from rest_framework.permissions import BasePermission
from rest_framework.exceptions import PermissionDenied, AuthenticationFailed
import jwt

class ClientPermission(BasePermission):
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
            raise AuthenticationFailed("Authentication credentials were not provided.")

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("Token has expired")
        except jwt.InvalidTokenError:
            raise AuthenticationFailed("Invalid token")
        

        if payload.get("role_name") == "admin":
        # Admin có thể truy cập tất cả tài nguyên và phương thức
         return True

        
        if payload.get("role_name") != "client" :
            raise PermissionDenied(f"You are not authorized as a client. Current role: {payload.get('role_name')}")

        allowed_actions = {
            "cart": ["GET", "POST", "PUT", "DELETE"],
            "cartline": ["GET", "POST", "PUT", "DELETE"],
            "favorites": ["GET", "POST", "PUT", "DELETE"],
            "favoriteline": ["GET", "POST", "PUT", "DELETE"],
            "salesorder": ["POST", "GET"],
            "salesorderline": ["POST", "GET"],
            "finishedproducts": ["GET"],
            "payment": ["POST", "GET"],
        }

        entity_name = None
        if hasattr(view, 'queryset'):
            entity_name = view.queryset.model._meta.model_name.lower()
        elif hasattr(view, 'serializer_class'):
            entity_name = view.serializer_class.Meta.model._meta.model_name.lower()

        if not entity_name or entity_name not in allowed_actions or request.method not in allowed_actions[entity_name]:
            raise PermissionDenied(f"Permission denied for entity '{entity_name}' with method '{request.method}'. Allowed methods are: {allowed_actions.get(entity_name, [])}.")

        return True
