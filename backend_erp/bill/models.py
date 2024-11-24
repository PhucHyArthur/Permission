from django.db import models
from supplier.models import Suppliers
from db_diy.models import Employees
from order.models import PurchaseOrder
from db_diy.models import Clients
from order.models import SalesOrder 

class PurchasesBill(models.Model):
    id = models.AutoField(primary_key=True)
    purchases_order = models.OneToOneField(PurchaseOrder, on_delete=models.CASCADE)
    invoice_name = models.CharField(max_length=255)
    invoice_number = models.CharField(max_length=255)
    employee = models.ForeignKey(Employees, on_delete=models.SET_NULL, null=True)
    supplier = models.ForeignKey(Suppliers, on_delete=models.SET_NULL, null=True)
    created_date = models.DateField()
    due = models.DateField()
    sub_total = models.IntegerField()
    tax_rate = models.IntegerField()
    tax_amount = models.IntegerField()
    total_amount = models.IntegerField()
    total_amount_text = models.CharField(max_length=255)
    status = models.CharField(max_length=100)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Purchase Bill {self.invoice_number} - Supplier: {self.supplier.name}"
    
class SalesBill(models.Model):
    id = models.AutoField(primary_key=True)
    sales_order = models.OneToOneField(SalesOrder, on_delete=models.CASCADE) 
    invoice_name = models.CharField(max_length=255)
    invoice_number = models.CharField(max_length=255)
    employee = models.ForeignKey(Employees, on_delete=models.SET_NULL, null=True)
    client = models.ForeignKey(Clients, on_delete=models.SET_NULL, null=True)
    created_date = models.DateField()
    due = models.DateField()
    sub_total = models.IntegerField()
    tax_rate = models.IntegerField()
    tax_amount = models.IntegerField()
    total_amount = models.IntegerField()
    total_amount_text = models.CharField(max_length=255)
    status = models.CharField(max_length=100)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Sales Bill {self.invoice_number} - Client: {self.client.name}"

