from rest_framework import viewsets

from backend_erp.permission import IsAuthenticatedWithJWT, TokenMatchesOASRequirements
from .models import Favorites, FavoriteLine
from .serializers import FavoritesSerializer, FavoriteLineSerializer
from backend_erp.clientPermission import ClientPermission

class FavoritesViewSet(viewsets.ModelViewSet):
    queryset = Favorites.objects.all()
    serializer_class = FavoritesSerializer
    permission_classes = [IsAuthenticatedWithJWT, ClientPermission]

class FavoriteLineViewSet(viewsets.ModelViewSet):
    queryset = FavoriteLine.objects.all()
    serializer_class = FavoriteLineSerializer
    permission_classes = [IsAuthenticatedWithJWT, ClientPermission]

    
