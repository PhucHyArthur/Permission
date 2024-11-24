from django.urls import path
from .views import WarehouseViewSet, ZoneViewSet, RackViewSet, LocationViewSet, RawMaterialsViewSet, FinishedProductsViewSet

# Warehouse routes
warehouse_list = WarehouseViewSet.as_view({'get': 'list'})
warehouse_create = WarehouseViewSet.as_view({'post': 'create'})
warehouse_detail = WarehouseViewSet.as_view({'get': 'retrieve'})
warehouse_update = WarehouseViewSet.as_view({'put': 'update'})
warehouse_delete = WarehouseViewSet.as_view({'delete': 'destroy','put': 'update'})
warehouse_restore = WarehouseViewSet.as_view({'patch': 'restore'})

# Zone routes
zone_list = ZoneViewSet.as_view({'get': 'list'})
zone_create = ZoneViewSet.as_view({'post': 'create'})
zone_detail = ZoneViewSet.as_view({'get': 'retrieve'})
zone_update = ZoneViewSet.as_view({'put': 'update'})
zone_delete = ZoneViewSet.as_view({'delete': 'destroy','put': 'update'})
zone_restore = ZoneViewSet.as_view({'patch': 'restore'})

# Rack routes
rack_list = RackViewSet.as_view({'get': 'list'})
rack_create = RackViewSet.as_view({'post': 'create'})
rack_detail = RackViewSet.as_view({'get': 'retrieve'})
rack_update = RackViewSet.as_view({'put': 'update'})
rack_delete = RackViewSet.as_view({'delete': 'destroy','put': 'update'})
rack_restore = RackViewSet.as_view({'patch': 'restore'})

# Location routes
location_list = LocationViewSet.as_view({'get': 'list'})
location_create = LocationViewSet.as_view({'post': 'create'})
location_detail = LocationViewSet.as_view({'get': 'retrieve'})
location_update = LocationViewSet.as_view({'put': 'update'})
location_delete = LocationViewSet.as_view({'delete': 'destroy','put': 'update'})
location_restore = LocationViewSet.as_view({'patch': 'restore'}) 

# RawMaterials routes
raw_materials_list = RawMaterialsViewSet.as_view({'get': 'list'})
raw_materials_create = RawMaterialsViewSet.as_view({'post': 'create'})
raw_materials_detail = RawMaterialsViewSet.as_view({'get': 'retrieve'})
raw_materials_update = RawMaterialsViewSet.as_view({'put': 'update'})
raw_materials_delete = RawMaterialsViewSet.as_view({'delete': 'destroy','put': 'update'})
raw_materials_restore = RawMaterialsViewSet.as_view({'patch': 'restore'})

# FinishedProducts routes
finished_products_list = FinishedProductsViewSet.as_view({'get': 'list'})
finished_products_create = FinishedProductsViewSet.as_view({'post': 'create'})
finished_products_detail = FinishedProductsViewSet.as_view({'get': 'retrieve'})
finished_products_update = FinishedProductsViewSet.as_view({'put': 'update'})
finished_products_delete = FinishedProductsViewSet.as_view({'delete': 'destroy','put': 'update'})
finished_products_restore = FinishedProductsViewSet.as_view({'patch': 'restore'}) 

urlpatterns = [
    # Warehouse routes
    path('warehouses/list/', warehouse_list, name='warehouse-list'),
    path('warehouses/add/', warehouse_create, name='warehouse-create'),
    path('warehouses/detail/<int:pk>/', warehouse_detail, name='warehouse-detail'),
    path('warehouses/update/<int:pk>/', warehouse_update, name='warehouse-update'),
    path('warehouses/delete/<int:pk>/', warehouse_delete, name='warehouse-delete'),
    path('warehouses/restore/<int:pk>/', warehouse_restore, name='warehouse-restore'),

    # Zone routes
    path('zones/list/', zone_list, name='zone-list'),
    path('zones/add/', zone_create, name='zone-create'),
    path('zones/detail/<int:pk>/', zone_detail, name='zone-detail'),
    path('zones/update/<int:pk>/', zone_update, name='zone-update'),
    path('zones/delete/<int:pk>/', zone_delete, name='zone-delete'),
    path('zones/restore/<int:pk>/', zone_restore, name='zone-restore'),

    # Rack routes
    path('racks/list/', rack_list, name='rack-list'),
    path('racks/add/', rack_create, name='rack-create'),
    path('racks/detail/<int:pk>/', rack_detail, name='rack-detail'),
    path('racks/update/<int:pk>/', rack_update, name='rack-update'),
    path('racks/delete/<int:pk>/', rack_delete, name='rack-delete'),
    path('racks/restore/<int:pk>/', rack_restore, name='rack-restore'),

    # Location routes
    path('locations/list/', location_list, name='location-list'),
    path('locations/add/', location_create, name='location-create'),
    path('locations/detail/<int:pk>/', location_detail, name='location-detail'),
    path('locations/update/<int:pk>/', location_update, name='location-update'),
    path('locations/delete/<int:pk>/', location_delete, name='location-delete'),
    path('locations/restore/<int:pk>/', location_restore, name='location-restore'),

    # Raw Materials routes
    path('raw-materials/list/', raw_materials_list, name='raw-materials-list'),
    path('raw-materials/add/', raw_materials_create, name='raw-materials-create'),
    path('raw-materials/detail/<int:pk>/', raw_materials_detail, name='raw-materials-detail'),
    path('raw-materials/update/<int:pk>/', raw_materials_update, name='raw-materials-update'),
    path('raw-materials/delete/<int:pk>/', raw_materials_delete, name='raw-materials-delete'),
    path('raw-materials/restore/<int:pk>/', raw_materials_restore, name='raw-materials-restore'),

    # Finished Products routes
    path('finished-products/list/', finished_products_list, name='finished-products-list'),
    path('finished-products/add/', finished_products_create, name='finished-products-create'),
    path('finished-products/detail/<int:pk>/', finished_products_detail, name='finished-products-detail'),
    path('finished-products/update/<int:pk>/', finished_products_update, name='finished-products-update'),
    path('finished-products/delete/<int:pk>/', finished_products_delete, name='finished-products-delete'),
    path('finished-products/restore/<int:pk>/', finished_products_restore, name='finished-products-restore'),
]
