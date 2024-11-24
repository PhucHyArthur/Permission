from rest_framework import serializers
from .models import Aisle, Warehouse, Zone, Rack, Location, RawMaterials, FinishedProducts


class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = ['id', 'name', 'address', 'capacity', 'description', 'isDelete', 'isFulled']


class ZoneSerializer(serializers.ModelSerializer):
    warehouse = serializers.PrimaryKeyRelatedField(queryset=Warehouse.objects.all(), allow_null=True)

    class Meta:
        model = Zone
        fields = ['id', 'warehouse', 'name', 'capacity', 'description', 'isDelete', 'isFulled']

class AisleSerializer(serializers.ModelSerializer):
    zone = serializers.PrimaryKeyRelatedField(queryset=Zone.objects.all(), allow_null=True)

    class Meta:
        model = Aisle
        fields = ['id', 'zone', 'name', 'capacity', 'description', 'isDelete', 'isFulled']



class RackSerializer(serializers.ModelSerializer):
    aisle = serializers.PrimaryKeyRelatedField(queryset=Aisle.objects.all(), allow_null=True)

    class Meta:
        model = Rack
        fields = ['id', 'aisle', 'name', 'capacity', 'description', 'isDelete', 'isFulled']


class LocationSerializer(serializers.ModelSerializer):
    rack = serializers.PrimaryKeyRelatedField(queryset=Rack.objects.all(), allow_null=True)
    class Meta:
        model = Location
        fields = ['id', 'rack', 'bin_number', 'description', 'quantity', 'isDelete', 'isFulled']


class RawMaterialsSerializer(serializers.ModelSerializer):
    location = serializers.PrimaryKeyRelatedField(queryset=Location.objects.all(), allow_null=True)

    class Meta:
        model = RawMaterials
        fields = ['id', 'name', 'category', 'image', 'price_per_unit', 'unit', 'quantity_in_stock', 
                  'location', 'description', 'expired_date', 'isAvailable', 'isDelete']


class FinishedProductsSerializer(serializers.ModelSerializer):
    location = serializers.PrimaryKeyRelatedField(queryset=Location.objects.all(), allow_null=True)

    class Meta:
        model = FinishedProducts
        fields = ['id', 'name', 'category', 'selling_price', 'quantity_in_stock', 'location', 
                  'description', 'expired_date', 'main_image', 'sub_image_1', 'sub_image_2', 
                  'isAvailable', 'isDelete']
