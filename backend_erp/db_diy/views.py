from rest_framework import viewsets, status
from rest_framework.response import Response
from django.db.models import Q

from backend_erp.permission import IsAuthenticatedWithJWT, TokenMatchesOASRequirements
from .models import Role, RolePermission, Employees,Clients
from .serializers import RoleSerializer, EmployeesSerializer,ClientsSerializer
from rest_framework.exceptions import AuthenticationFailed
import jwt, datetime
from rest_framework.views import APIView

class RoleViewSet(viewsets.ViewSet):
    # permission_classes = [IsAuthenticatedWithJWT, TokenMatchesOASRequirements]
    # required_alternate_scopes = {
    #     "GET": [["read"]],
    #     "POST": [["create"], ["post", "widget"]],
    #     "PUT": [["update"], ["put", "widget"]],
    #     "DELETE": [["delete"], ["scope2", "scope3"]],
    # }

    def list(self, request):
        roles = Role.objects.all()
        serializer = RoleSerializer(roles, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        role = Role.objects.get(pk=pk)
        serializer = RoleSerializer(role)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = RoleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        role = Role.objects.get(pk=pk)
        serializer = RoleSerializer(role, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        role = Role.objects.get(pk=pk)
        role.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class EmployeesViewSet(viewsets.ModelViewSet):
    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializer
    permission_classes = [IsAuthenticatedWithJWT, TokenMatchesOASRequirements]
    required_alternate_scopes = {
        "GET": [["read"]],
        "POST": [["create"], ["post", "widget"]],
        "PUT": [["update"], ["put", "widget"]],
        "DELETE": [["delete"], ["scope2", "scope3"]],
    }


class ClientsViewSet(viewsets.ModelViewSet):
    queryset = Clients.objects.all()
    serializer_class = ClientsSerializer
    permission_classes = [IsAuthenticatedWithJWT, TokenMatchesOASRequirements]
    required_alternate_scopes = {
        "GET": [["read"]],
        "POST": [["create"], ["post", "widget"]],
        "PUT": [["update"], ["put", "widget"]],
        "DELETE": [["delete"], ["scope2", "scope3"]],
    }

#employees
class RegisterView(APIView):
    def post(self, request):
        serializer = EmployeesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    

class LoginView(APIView):
    def post(self, request):
       
        username_or_email = request.data.get('username') or request.data.get('email')
        password = request.data.get('password')


        if not username_or_email or not password:
            raise AuthenticationFailed('Username or email and password are required.')

        # Tìm kiếm người dùng theo email hoặc username
        user = Employees.objects.filter(
            Q(email=username_or_email) | Q(username=username_or_email)
        ).first()

        if not user:
            raise AuthenticationFailed('User not found.')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')

        payload = {
            'user_id': user.id,
            'user_name': user.username,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow(),
            'role_id': user.role.role_id,
            'role_name': user.role.role_name,
            'permissions': []
        }

        role_permissions = RolePermission.objects.filter(role=user.role)

        for role_permission in role_permissions:
            payload['permissions'].append({
                'entity_id': role_permission.entity.entity_id,
                'entity_name': role_permission.entity.entity_name,
                'view': role_permission.view,
                'create': role_permission.create,
                'edit': role_permission.edit,
                'delete': role_permission.delete,
                'full_access': role_permission.full_access
            })

    
        token = jwt.encode(payload, 'secret', algorithm='HS256')

       
        response = Response()
        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt': token
        }

        return response

     
class EmployeesView(APIView):
    permission_classes = [IsAuthenticatedWithJWT]
    def get(self, request):
        token=request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('Unauthenticated')
        
        try:
           payload = jwt.decode(token, 'secret', algorithms=['HS256'])

        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        user = Employees.objects.filter(id=payload['id']).first()
        serializer = EmployeesSerializer(user)
        return Response(serializer.data)
    
class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }
        return response
    

#clients
class ClientLoginView(APIView):
    def post(self, request):
        username_or_email = request.data.get('username') or request.data.get('email')
        password = request.data.get('password')

        if not username_or_email or not password:
            raise AuthenticationFailed('Username or email and password are required.')

      
        client = Clients.objects.filter(
            Q(email=username_or_email) | Q(username=username_or_email)
        ).first()

        if not client:
            raise AuthenticationFailed('Client not found.')

        if not client.check_password(password):
            raise AuthenticationFailed('Incorrect password!')

        # Payload JWT
        payload = {
            'user_id': client.id,
            'user_name': client.username,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow(),
            'role_name': 'client',
        }

        
        token = jwt.encode(payload, 'secret', algorithm='HS256')

        response = Response()
        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt': token
        }

        return response

class ClientRegisterView(APIView):
    def post(self, request):
        serializer = ClientsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class ClientsView(APIView):
    permission_classes = [IsAuthenticatedWithJWT]
    def get(self, request):
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('Unauthenticated')

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        client = Clients.objects.filter(id=payload['user_id']).first()
        serializer = ClientsSerializer(client)
        return Response(serializer.data)

class ClientLogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }
        return response
