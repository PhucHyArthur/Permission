from rest_framework import serializers
from .models import SalesOrder, SalesOrderLine, PurchaseOrder, PurchaseOrderLine
from db_diy.models import Clients
from inventory.models import FinishedProducts, RawMaterials
from supplier.models import Suppliers

class SalesOrderSerializer(serializers.ModelSerializer):
    client = serializers.PrimaryKeyRelatedField(queryset=Clients.objects.all(), allow_null=True)
    
    class Meta:
        model = SalesOrder
        fields = [
            'id', 'order_number', 'client', 'order_date', 'due_date', 
            'status', 'total_amount', 'remarks', 'is_deleted', 'created_at'
        ]

class SalesOrderLineSerializer(serializers.ModelSerializer):
    sales_order = serializers.PrimaryKeyRelatedField(queryset=SalesOrder.objects.all(), allow_null=True)
    product = serializers.PrimaryKeyRelatedField(queryset=FinishedProducts.objects.all(), allow_null=True)
    
    class Meta:
        model = SalesOrderLine
        fields = [
            'id', 'sales_order', 'product', 'quantity', 'unit_price', 
            'line_total', 'created_at'
        ]

class PurchaseOrderSerializer(serializers.ModelSerializer):
    supplier = serializers.PrimaryKeyRelatedField(queryset=Suppliers.objects.all(), allow_null=True)
    
    class Meta:
        model = PurchaseOrder
        fields = [
            'id', 'order_number', 'supplier', 'order_date', 'due_date', 
            'status', 'total_amount', 'remarks', 'is_deleted', 'created_at'
        ]

class PurchaseOrderLineSerializer(serializers.ModelSerializer):
    purchase_order = serializers.PrimaryKeyRelatedField(queryset=PurchaseOrder.objects.all(), allow_null=True)
    material = serializers.PrimaryKeyRelatedField(queryset=RawMaterials.objects.all(), allow_null=True)
    
    class Meta:
        model = PurchaseOrderLine
        fields = [
            'id', 'purchase_order', 'material', 'quantity', 'unit_price', 
            'line_total', 'created_at'
        ]
