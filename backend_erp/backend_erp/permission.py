from rest_framework.permissions import BasePermission
from rest_framework.exceptions import AuthenticationFailed
import jwt
import os
from rest_framework.exceptions import PermissionDenied

class IsAuthenticatedWithJWT(BasePermission):
    def has_permission(self, request, view):
      
        token = request.COOKIES.get('jwt') or self.get_token_from_authorization_header(request)

        if not token:
            raise AuthenticationFailed("Authentication credentials were not provided.") 

        try:
            # Giải mã JWT token
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("Token has expired")
        except jwt.InvalidTokenError:
            raise AuthenticationFailed("Invalid token")

        # Đặt payload vào request để có thể sử dụng trong view
        request.user_payload = payload
        return True

    def get_token_from_authorization_header(self, request):
    
        auth_header = request.headers.get('Authorization', None)
        if auth_header:
            parts = auth_header.split()
            if len(parts) == 2 and parts[0].lower() == 'bearer':
                return parts[1]
        return None


class TokenMatchesOASRequirements(BasePermission):
    required_alternate_scopes = {}

    def get_token_from_authorization_header(self, request):
    
        auth = request.headers.get('Authorization', None)
        if not auth:
            return None
        parts = auth.split()
        if len(parts) == 2 and parts[0].lower() == 'bearer':
            return parts[1]
        return None

    def has_permission(self, request, view):
    
        token = request.COOKIES.get('jwt') or self.get_token_from_authorization_header(request)
        
        if not token:
            raise PermissionDenied("No token provided")
        
        # Giải mã token
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise PermissionDenied("Token has expired")
        except jwt.InvalidTokenError:
            raise PermissionDenied("Invalid token")
        


       # Kiểm tra xem user có phải là admin không
        if payload['role_name'] == 'admin':
            return True
        entity_name = None

       
        if hasattr(view, 'queryset'):
        
            model = view.queryset.model
            entity_name = model._meta.model_name
        elif hasattr(view, 'serializer_class'):

            model = view.serializer_class.Meta.model
            entity_name = model._meta.model_name
        
        if not entity_name:
            raise PermissionDenied("Entity name not found")

      
        entity_permissions = next((perm for perm in payload['permissions'] if perm['entity_name'] == entity_name), None)

        if not entity_permissions:
            raise PermissionDenied(f"No permissions found for entity: {entity_name}")

       
        if request.method == "GET" and not entity_permissions['view']:
            raise PermissionDenied("Insufficient permission for GET")

        if request.method == "POST" and not entity_permissions['create']:
            raise PermissionDenied("Insufficient permission for POST")

        if request.method == "PUT" and not entity_permissions['edit']:
            raise PermissionDenied("Insufficient permission for PUT")

        if request.method == "DELETE" and not entity_permissions['delete']:
            raise PermissionDenied("Insufficient permission for DELETE")

        return True
    