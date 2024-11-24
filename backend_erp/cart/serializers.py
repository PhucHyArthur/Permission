from rest_framework import serializers
from .models import Cart, CartLine
from inventory.models import FinishedProducts
from db_diy.models import Clients

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id', 'client']

class CartLineSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=FinishedProducts.objects.all(), allow_null=True)
    cart = serializers.PrimaryKeyRelatedField(queryset=Cart.objects.all(), allow_null=True)

    class Meta:
        model = CartLine
        fields = ['id', 'cart', 'product', 'quantity', 'unit_price']
