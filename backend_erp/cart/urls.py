from django.urls import path
from .views import CartViewSet, CartLineViewSet

# Cart
cart_list = CartViewSet.as_view({'get': 'list'})
cart_create = CartViewSet.as_view({'post': 'create'})
cart_detail = CartViewSet.as_view({'get': 'retrieve'})
cart_update = CartViewSet.as_view({'put': 'update'})
cart_delete = CartViewSet.as_view({'delete': 'destroy','put': 'update'})
cart_restore = CartViewSet.as_view({'patch': 'restore'})  

# CartLine
cart_line_list = CartLineViewSet.as_view({'get': 'list'})
cart_line_create = CartLineViewSet.as_view({'post': 'create'})
cart_line_detail = CartLineViewSet.as_view({'get': 'retrieve'})
cart_line_update = CartLineViewSet.as_view({'put': 'update'})
cart_line_delete = CartLineViewSet.as_view({'delete': 'destroy','put': 'update'})
cart_line_restore = CartLineViewSet.as_view({'patch': 'restore'})  

urlpatterns = [
    # Cart routes
    path('carts/list/', cart_list, name='carts-list'),
    path('carts/add/', cart_create, name='carts-create'),
    path('carts/detail/<int:pk>/', cart_detail, name='carts-detail'),
    path('carts/update/<int:pk>/', cart_update, name='carts-update'),
    path('carts/delete/<int:pk>/', cart_delete, name='carts-delete'),
    path('carts/restore/<int:pk>/', cart_restore, name='carts-restore'),

    # CartLine routes
    path('carts-lines/list/', cart_line_list, name='carts-line-list'),
    path('carts-lines/add/', cart_line_create, name='carts-line-create'),
    path('carts-lines/detail/<int:pk>/', cart_line_detail, name='carts-line-detail'),
    path('carts-lines/update/<int:pk>/', cart_line_update, name='carts-line-update'),
    path('carts-lines/delete/<int:pk>/', cart_line_delete, name='carts-line-delete'),
    path('carts-lines/restore/<int:pk>/', cart_line_restore, name='carts-line-restore'),
]
