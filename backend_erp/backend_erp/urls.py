from django.contrib import admin
from django.urls import path, include, re_path
from django.http import JsonResponse
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view # type: ignore
from drf_yasg import openapi # type: ignore
# Định nghĩa API chào mừng hoặc trang chủ
def welcome(request):
    data = {
        "message": "Welcome to the ERP System API!"
    }
    return JsonResponse(data)

schema_view = get_schema_view(
    openapi.Info(
        title="API Documentation",
        default_version='v1',
        description="Documentation for the API endpoints",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="support@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('db_diy.urls')),
    path('api/', include('inventory.urls')),
    path('api/', include('supplier.urls')),
    path('api/', include('order.urls')),
    path('api/', include('bill.urls')),
    path('api/', include('cart.urls')),
    path('api/', include('favorite.urls')),
    # path('payment/', include('payment.urls')),
    
    # Định tuyến API chào mừng (trang chủ)
    path('', welcome, name='home'),  # Trang chủ trả về thông điệp chào mừng

    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

# Thêm cấu hình cho static và media file
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
