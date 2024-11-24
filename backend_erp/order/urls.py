from django.urls import path
from .views import SalesOrderViewSet, SalesOrderLineViewSet, PurchaseOrderViewSet, PurchaseOrderLineViewSet

# SalesOrder routes
sales_order_list = SalesOrderViewSet.as_view({'get': 'list'})
sales_order_create = SalesOrderViewSet.as_view({'post': 'create'})
sales_order_detail = SalesOrderViewSet.as_view({'get': 'retrieve'})
sales_order_update = SalesOrderViewSet.as_view({'put': 'update'})
sales_order_delete = SalesOrderViewSet.as_view({'delete': 'destroy','put':'update'})
sales_order_restore = SalesOrderViewSet.as_view({'patch': 'restore'})
# SalesOrderLine routes
sales_order_line_list = SalesOrderLineViewSet.as_view({'get': 'list'})
sales_order_line_create = SalesOrderLineViewSet.as_view({'post': 'create'})
sales_order_line_detail = SalesOrderLineViewSet.as_view({'get': 'retrieve'})
sales_order_line_update = SalesOrderLineViewSet.as_view({'put': 'update'})
sales_order_line_delete = SalesOrderLineViewSet.as_view({'delete': 'destroy','put':'update'})
sales_order_line_restore = SalesOrderLineViewSet.as_view({'patch': 'restore'})  
# PurchaseOrder routes
purchase_order_list = PurchaseOrderViewSet.as_view({'get': 'list'})
purchase_order_create = PurchaseOrderViewSet.as_view({'post': 'create'})
purchase_order_detail = PurchaseOrderViewSet.as_view({'get': 'retrieve'})
purchase_order_update = PurchaseOrderViewSet.as_view({'put': 'update'})
purchase_order_delete = PurchaseOrderViewSet.as_view({'delete': 'destroy','put':'update'})
purchase_order_restore = PurchaseOrderViewSet.as_view({'patch': 'restore'})  

# PurchaseOrderLine routes
purchase_order_line_list = PurchaseOrderLineViewSet.as_view({'get': 'list'})
purchase_order_line_create = PurchaseOrderLineViewSet.as_view({'post': 'create'})
purchase_order_line_detail = PurchaseOrderLineViewSet.as_view({'get': 'retrieve'})
purchase_order_line_update = PurchaseOrderLineViewSet.as_view({'put': 'update'})
purchase_order_line_delete = PurchaseOrderLineViewSet.as_view({'delete': 'destroy','put':'update'})
purchase_order_line_restore = PurchaseOrderLineViewSet.as_view({'patch': 'restore'})  

urlpatterns = [
    # SalesOrder routes
    path('sales-orders/list/', sales_order_list, name='sales-order-list'),
    path('sales-orders/add/', sales_order_create, name='sales-order-create'),
    path('sales-orders/detail/<int:pk>/', sales_order_detail, name='sales-order-detail'),
    path('sales-orders/update/<int:pk>/', sales_order_update, name='sales-order-update'),
    path('sales-orders/delete/<int:pk>/', sales_order_delete, name='sales-order-delete'),
    path('sales-orders/restore/<int:pk>/', sales_order_restore, name='sales-order-restore'),

    # SalesOrderLine routes
    path('sales-orders-lines/list/', sales_order_line_list, name='sales-order-line-list'),
    path('sales-orders-lines/add/', sales_order_line_create, name='sales-order-line-create'),
    path('sales-orders-lines/detail/<int:pk>/', sales_order_line_detail, name='sales-order-line-detail'),
    path('sales-orders-lines/update/<int:pk>/', sales_order_line_update, name='sales-order-line-update'),
    path('sales-orders-lines/delete/<int:pk>/', sales_order_line_delete, name='sales-order-line-delete'),
    path('sales-orders-lines/restore/<int:pk>/', sales_order_line_restore, name='sales-order-line-restore'),

    # PurchaseOrder routes
    path('purchases-orders/list/', purchase_order_list, name='purchases-order-list'),
    path('purchases-orders/add/', purchase_order_create, name='purchases-order-create'),
    path('purchases-orders/detail/<int:pk>/', purchase_order_detail, name='purchase-order-detail'),
    path('purchases-orders/update/<int:pk>/', purchase_order_update, name='purchase-order-update'),
    path('purchases-orders/delete/<int:pk>/', purchase_order_delete, name='purchase-order-delete'),
    path('purchases-orders/restore/<int:pk>/', purchase_order_restore, name='purchase-order-restore'),

    # PurchaseOrderLine routes
    path('purchases-orders-lines/list/', purchase_order_line_list, name='purchases-order-line-list'),
    path('purchases-orders-lines/add/', purchase_order_line_create, name='purchases-order-line-create'),
    path('purchases-orders-lines/detail/<int:pk>/', purchase_order_line_detail, name='purchases-order-line-detail'),
    path('purchases-orders-lines/update/<int:pk>/', purchase_order_line_update, name='purchases-order-line-update'),
    path('purchases-orders-lines/delete/<int:pk>/', purchase_order_line_delete, name='purchases-order-line-delete'),
    path('purchases-orders-lines/restore/<int:pk>/', purchase_order_line_restore, name='purchases-order-line-restore'),
]
