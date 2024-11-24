from django.contrib import admin

from backend_erp.bill.models import PurchasesBill,SalesBill

# Đăng ký models
admin.site.register(PurchasesBill)
admin.site.register(SalesBill)
