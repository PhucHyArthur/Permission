from django.urls import path
from .views import PurchasesBillViewSet, SalesBillViewSet

# PurchasesBill
purchases_bill_list = PurchasesBillViewSet.as_view({'get': 'list'})
purchases_bill_create = PurchasesBillViewSet.as_view({'post': 'create'})
purchases_bill_detail = PurchasesBillViewSet.as_view({'get': 'retrieve'})
purchases_bill_update = PurchasesBillViewSet.as_view({'put': 'update'})
purchases_bill_delete = PurchasesBillViewSet.as_view({'put': 'update','delete': 'destroy'})
purchases_bill_restore = PurchasesBillViewSet.as_view({'patch': 'restore'}) 

# SalesBill
sales_bill_list = SalesBillViewSet.as_view({'get': 'list'})
sales_bill_create = SalesBillViewSet.as_view({'post': 'create'})
sales_bill_detail = SalesBillViewSet.as_view({'get': 'retrieve'})
sales_bill_update = SalesBillViewSet.as_view({'put': 'update'})
sales_bill_delete = SalesBillViewSet.as_view({'delete': 'destroy', 'put': 'update'})
sales_bill_restore = SalesBillViewSet.as_view({'patch': 'restore'}) 

urlpatterns = [
    # PurchasesBill routes
    path('purchases-bills/list/', purchases_bill_list, name='purchases-bill-list'),
    path('purchases-bills/add/', purchases_bill_create, name='purchases-bill-create'),
    path('purchases-bills/detail/<int:pk>/', purchases_bill_detail, name='purchases-bill-detail'),
    path('purchases-bills/update/<int:pk>/', purchases_bill_update, name='purchases-bill-update'),
    path('purchases-bills/delete/<int:pk>/', purchases_bill_delete, name='purchases-bill-delete'),
    path('purchases-bills/restore/<int:pk>/', purchases_bill_restore, name='purchases-bill-restore'), 

    # SalesBill routes
    path('sales-bills/list/', sales_bill_list, name='sales-bill-list'),
    path('sales-bills/add/', sales_bill_create, name='sales-bill-create'),
    path('sales-bills/detail/<int:pk>/', sales_bill_detail, name='sales-bill-detail'),
    path('sales-bills/update/<int:pk>/', sales_bill_update, name='sales-bill-update'),
    path('sales-bills/delete/<int:pk>/', sales_bill_delete, name='sales-bill-delete'),
    path('sales-bills/restore/<int:pk>/', sales_bill_restore, name='sales-bill-restore'), 
]
