from rest_framework import serializers
from .models import PurchasesBill, SalesBill
from order.models import PurchaseOrder, SalesOrder
from db_diy.models import Employees, Clients
from supplier.models import Suppliers

class PurchasesBillSerializer(serializers.ModelSerializer):
    # Liên kết với PurchaseOrder, Employee, và Supplier
    purchases_order = serializers.PrimaryKeyRelatedField(queryset=PurchaseOrder.objects.all())
    employee = serializers.PrimaryKeyRelatedField(queryset=Employees.objects.all(), required=False, allow_null=True)
    supplier = serializers.PrimaryKeyRelatedField(queryset=Suppliers.objects.all(), required=False, allow_null=True)

    class Meta:
        model = PurchasesBill
        fields = [
            'id', 'purchases_order', 'invoice_name', 'invoice_number', 'employee', 'supplier', 
            'created_date', 'due', 'sub_total', 'tax_rate', 'tax_amount', 'total_amount', 
            'total_amount_text', 'status', 'is_deleted', 'created_at'
        ]

class SalesBillSerializer(serializers.ModelSerializer):
    
    sales_order = serializers.PrimaryKeyRelatedField(queryset=SalesOrder.objects.all(), allow_null=True)
    employee = serializers.PrimaryKeyRelatedField(queryset=Employees.objects.all(), allow_null=True)
    client = serializers.PrimaryKeyRelatedField(queryset=Clients.objects.all(), allow_null=True)

    class Meta:
        model = SalesBill
        fields = [
            'id', 'sales_order', 'invoice_name', 'invoice_number', 'employee', 'client', 
            'created_date', 'due', 'sub_total', 'tax_rate', 'tax_amount', 'total_amount', 
            'total_amount_text', 'status', 'is_deleted', 'created_at'
        ]
