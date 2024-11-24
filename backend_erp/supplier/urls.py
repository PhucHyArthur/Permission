from django.urls import path
from .views import SupplierViewSet, RepresentativeViewSet, BankingDetailViewSet

# Supplier routes
supplier_list = SupplierViewSet.as_view({'get': 'list'})
supplier_create = SupplierViewSet.as_view({'post': 'create'})
supplier_detail = SupplierViewSet.as_view({'get': 'retrieve'})
supplier_update = SupplierViewSet.as_view({'put': 'update'})
supplier_delete = SupplierViewSet.as_view({'delete': 'destroy','put':'update'})
supplier_restore = SupplierViewSet.as_view({'patch': 'restore'})  

# Representative routes
representative_list = RepresentativeViewSet.as_view({'get': 'list'})
representative_create = RepresentativeViewSet.as_view({'post': 'create'})
representative_detail = RepresentativeViewSet.as_view({'get': 'retrieve'})
representative_update = RepresentativeViewSet.as_view({'put': 'update'})
representative_delete = RepresentativeViewSet.as_view({'delete': 'destroy','put':'update'})
representative_restore = RepresentativeViewSet.as_view({'patch': 'restore'}) 

# BankingDetail routes
bankingdetail_list = BankingDetailViewSet.as_view({'get': 'list'})
bankingdetail_create = BankingDetailViewSet.as_view({'post': 'create'})
bankingdetail_detail = BankingDetailViewSet.as_view({'get': 'retrieve'})
bankingdetail_update = BankingDetailViewSet.as_view({'put': 'update'})
bankingdetail_delete = BankingDetailViewSet.as_view({'delete': 'destroy','put':'update'})
bankingdetail_restore = BankingDetailViewSet.as_view({'patch': 'restore'}) 

urlpatterns = [
    # Supplier routes
    path('supplier/list/', supplier_list, name='supplier-list'),
    path('supplier/add/', supplier_create, name='supplier-create'),
    path('supplier/detail/<int:pk>/', supplier_detail, name='supplier-detail'),
    path('supplier/update/<int:pk>/', supplier_update, name='supplier-update'),
    path('supplier/delete/<int:pk>/', supplier_delete, name='supplier-delete'),
    path('supplier/restore/<int:pk>/', supplier_restore, name='supplier-restore'),

    # Representative routes
    path('representative/list/', representative_list, name='representative-list'),
    path('representative/add/', representative_create, name='representative-create'),
    path('representative/detail/<int:pk>/', representative_detail, name='representative-detail'),
    path('representative/update/<int:pk>/', representative_update, name='representative-update'),
    path('representative/delete/<int:pk>/', representative_delete, name='representative-delete'),
    path('representative/restore/<int:pk>/', representative_restore, name='representative-restore'),

    # BankingDetail routes
    path('bankingdetail/list/', bankingdetail_list, name='bankingdetail-list'),
    path('bankingdetail/add/', bankingdetail_create, name='bankingdetail-create'),
    path('bankingdetail/detail/<int:pk>/', bankingdetail_detail, name='bankingdetail-detail'),
    path('bankingdetail/update/<int:pk>/', bankingdetail_update, name='bankingdetail-update'),
    path('bankingdetail/delete/<int:pk>/', bankingdetail_delete, name='bankingdetail-delete'),
    path('bankingdetail/restore/<int:pk>/', bankingdetail_restore, name='bankingdetail-restore'),
]
