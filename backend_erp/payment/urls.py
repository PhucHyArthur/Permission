from django.urls import path
from .views import PaymentViewSet


payment_execute_paypal = PaymentViewSet.as_view({'get': 'execute_paypal_payment'})
payment_cancel_paypal = PaymentViewSet.as_view({'get': 'cancel_paypal_payment'})
payment_create_paypal = PaymentViewSet.as_view({'post': 'create_paypal_payment'})

urlpatterns = [

    # PayPal-specific routes
    path('paypal/create/<int:pk>/', payment_create_paypal, name='payment-create-paypal'),
    path('paypal/execute/<int:pk>/', payment_execute_paypal, name='payment-execute-paypal'),
    path('paypal/cancel/<int:pk>/', payment_cancel_paypal, name='payment-cancel-paypal'),
]
