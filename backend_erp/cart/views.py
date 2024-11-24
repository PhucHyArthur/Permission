from rest_framework import viewsets

from backend_erp.clientPermission import ClientPermission
from backend_erp.permission import IsAuthenticatedWithJWT
from .models import Cart, CartLine
from .serializers import CartSerializer, CartLineSerializer

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticatedWithJWT, ClientPermission]

class CartLineViewSet(viewsets.ModelViewSet):
    queryset = CartLine.objects.all()
    serializer_class = CartLineSerializer
    permission_classes = [IsAuthenticatedWithJWT, ClientPermission]

