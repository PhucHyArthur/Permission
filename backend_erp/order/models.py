import os
import sys
from django.db import models
from db_diy.models import Clients
from inventory.models import FinishedProducts, RawMaterials
from supplier.models import Suppliers


class SalesOrder(models.Model):
    id = models.AutoField(primary_key=True)
    order_number = models.CharField(max_length=255, unique=True)
    client = models.ForeignKey(Clients, on_delete=models.CASCADE)
    order_date = models.DateField()
    due_date = models.DateField()
    status = models.CharField(max_length=100)
    total_amount = models.IntegerField()
    remarks = models.TextField(blank=True, null=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.order_number} - Customer: {self.customer}"


class SalesOrderLine(models.Model):
    id = models.AutoField(primary_key=True)
    sales_order = models.ForeignKey(SalesOrder, on_delete=models.CASCADE, related_name='order_lines')
    product = models.ForeignKey(FinishedProducts, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    unit_price = models.IntegerField()
    line_total = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Line for Order {self.sales_order.order_number} - Product: {self.product}"


class PurchaseOrder(models.Model):
    id = models.AutoField(primary_key=True)
    order_number = models.CharField(max_length=255, unique=True)
    supplier = models.ForeignKey(Suppliers, on_delete=models.CASCADE)
    order_date = models.DateField()
    due_date = models.DateField()
    status = models.CharField(max_length=100)
    total_amount = models.IntegerField()
    remarks = models.TextField(blank=True, null=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Purchase Order {self.order_number} - Supplier: {self.supplier}"


class PurchaseOrderLine(models.Model):
    id = models.AutoField(primary_key=True)
    purchase_order = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE, related_name='order_lines')
    material = models.ForeignKey(RawMaterials, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    unit_price = models.IntegerField()
    line_total = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Line for Purchase Order {self.purchase_order.order_number} - Material: {self.material}"
