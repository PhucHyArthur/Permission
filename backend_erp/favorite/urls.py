from django.urls import path
from .views import FavoritesViewSet, FavoriteLineViewSet

# Favorites routes
favorites_list = FavoritesViewSet.as_view({'get': 'list'})
favorites_create = FavoritesViewSet.as_view({'post': 'create'})
favorites_detail = FavoritesViewSet.as_view({'get': 'retrieve'})
favorites_update = FavoritesViewSet.as_view({'put': 'update'})
favorites_delete = FavoritesViewSet.as_view({'delete': 'destroy','put':'update'})
favorites_restore = FavoritesViewSet.as_view({'patch': 'restore'})

# FavoriteLine routes
favorite_line_list = FavoriteLineViewSet.as_view({'get': 'list'})
favorite_line_create = FavoriteLineViewSet.as_view({'post': 'create'})
favorite_line_detail = FavoriteLineViewSet.as_view({'get': 'retrieve'})
favorite_line_update = FavoriteLineViewSet.as_view({'put': 'update'})
favorite_line_delete = FavoriteLineViewSet.as_view({'delete': 'destroy','put':'update'})
favorite_line_restore = FavoriteLineViewSet.as_view({'patch': 'restore'}) 

urlpatterns = [
    # Favorites routes
    path('favorites/list/', favorites_list, name='favorites-list'),
    path('favorites/add/', favorites_create, name='favorites-create'),
    path('favorites/detail/<int:pk>/', favorites_detail, name='favorites-detail'),
    path('favorites/update/<int:pk>/', favorites_update, name='favorites-update'),
    path('favorites/delete/<int:pk>/', favorites_delete, name='favorites-delete'),
    path('favorites/restore/<int:pk>/', favorites_restore, name='favorites-restore'),

    # FavoriteLine routes
    path('favorites-lines/list/', favorite_line_list, name='favorites-line-list'),
    path('favorites-lines/add/', favorite_line_create, name='favorites-line-create'),
    path('favorites-lines/detail/<int:pk>/', favorite_line_detail, name='favorites-line-detail'),
    path('favorites-lines/update/<int:pk>/', favorite_line_update, name='favorites-line-update'),
    path('favorites-lines/delete/<int:pk>/', favorite_line_delete, name='favorites-line-delete'),
    path('favorites-lines/restore/<int:pk>/', favorite_line_restore, name='favorites-line-restore'),
]
