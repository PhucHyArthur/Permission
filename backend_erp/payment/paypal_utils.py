import paypalrestsdk # type: ignore
from django.conf import settings

# Cấu hình PayPal SDK
paypalrestsdk.configure({
    "mode": settings.PAYPAL_MODE,  # Chế độ sandbox hoặc live
    "client_id": settings.PAYPAL_CLIENT_ID,
    "client_secret": settings.PAYPAL_CLIENT_SECRET
})
