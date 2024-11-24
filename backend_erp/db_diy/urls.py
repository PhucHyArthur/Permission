from django.urls import path
from .views import ClientLoginView, ClientLogoutView, ClientRegisterView, ClientsViewSet, RoleViewSet, EmployeesViewSet
from .views import RegisterView, LoginView, EmployeesView, LogoutView

# Role routes
role_list = RoleViewSet.as_view({'get': 'list'})
role_create = RoleViewSet.as_view({'post': 'create'})
role_detail = RoleViewSet.as_view({'get': 'retrieve'})
role_update = RoleViewSet.as_view({'put': 'update'})
role_delete = RoleViewSet.as_view({'delete': 'destroy','put': 'update'})
role_restore = RoleViewSet.as_view({'patch': 'restore'}) 

# Employee routes
employees_list = EmployeesViewSet.as_view({'get': 'list'})
employees_create = EmployeesViewSet.as_view({'post': 'create'})
employees_detail = EmployeesViewSet.as_view({'get': 'retrieve'})
employees_update = EmployeesViewSet.as_view({'put': 'update'})
employees_delete = EmployeesViewSet.as_view({'delete': 'destroy','put': 'update'})
employees_restore = EmployeesViewSet.as_view({'patch': 'restore'}) 

# Client routes
clients_list = ClientsViewSet.as_view({'get': 'list'})
clients_create = ClientsViewSet.as_view({'post': 'create'})
clients_detail = ClientsViewSet.as_view({'get': 'retrieve'})
clients_update = ClientsViewSet.as_view({'put': 'update'})
clients_delete = ClientsViewSet.as_view({'delete': 'destroy','put': 'update'})
clients_restore = ClientsViewSet.as_view({'patch': 'restore'}) 

urlpatterns = [
    # Role routes
    path('settings/roles/list/', role_list, name='role-list'),
    path('settings/roles/add/', role_create, name='role-create'),
    path('settings/roles/detail/<int:pk>/', role_detail, name='role-detail'),
    path('settings/roles/update/<int:pk>/', role_update, name='role-update'),
    path('settings/roles/delete/<int:pk>/', role_delete, name='role-delete'),
    path('settings/roles/restore/<int:pk>/', role_restore, name='role-restore'),

    # Employee routes
    path('employees/list/', employees_list, name='employees-list'),
    path('employees/add/', employees_create, name='employees-create'),
    path('employees/detail/<int:pk>/', employees_detail, name='employees-detail'),
    path('employees/update/<int:pk>/', employees_update, name='employees-update'),
    path('employees/delete/<int:pk>/', employees_delete, name='employees-delete'),
    path('employees/restore/<int:pk>/', employees_restore, name='employees-restore'),

    # Client routes
    path('clients/list/', clients_list, name='clients-list'),
    path('clients/add/', clients_create, name='clients-create'),
    path('clients/detail/<int:pk>/', clients_detail, name='clients-detail'),
    path('clients/update/<int:pk>/', clients_update, name='clients-update'),
    path('clients/delete/<int:pk>/', clients_delete, name='clients-delete'),
    path('clients/restore/<int:pk>/', clients_restore, name='clients-restore'),

    # Client authentication routes
    path('auth/client/register/', ClientRegisterView.as_view(), name='client-register'),
    path('auth/client/login/', ClientLoginView.as_view(), name='client-login'),
    path('auth/client/logout/', ClientLogoutView.as_view(), name='client-logout'),

    # Employee authentication routes
    path('auth/employee/register/', RegisterView.as_view(), name='employee-register'),
    path('auth/employee/login/', LoginView.as_view(), name='employee-login'),
    path('auth/employee/logout/', LogoutView.as_view(), name='employee-logout'),
]
