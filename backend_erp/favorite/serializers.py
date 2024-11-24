from rest_framework import serializers
from .models import Favorites, FavoriteLine
from inventory.models import FinishedProducts
from db_diy.models import Clients

class FavoritesSerializer(serializers.ModelSerializer):
    client = serializers.PrimaryKeyRelatedField(queryset=Clients.objects.all(), allow_null=True)

    class Meta:
        model = Favorites
        fields = ['id', 'client']

class FavoriteLineSerializer(serializers.ModelSerializer):
    favorites = serializers.PrimaryKeyRelatedField(queryset=Favorites.objects.all(), allow_null=True)
    product = serializers.PrimaryKeyRelatedField(queryset=FinishedProducts.objects.all(), allow_null=True)

    class Meta:
        model = FavoriteLine
        fields = ['id', 'favorites', 'product']
