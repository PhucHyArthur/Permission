from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db import transaction
from django.conf import settings
from rest_framework.permissions import IsAuthenticated
from backend_erp.permission import IsAuthenticatedWithJWT
import paypalrestsdk # type: ignore
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from backend_erp.clientPermission import ClientPermission
from .models import Payment, SalesOrder
from .serializers import PaymentSerializer
import logging

# Configure logging
logger = logging.getLogger(__name__)

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticatedWithJWT, ClientPermission]

    @csrf_exempt  # Bỏ qua CSRF nếu cần
    @action(detail=True, methods=['post'])
    def create_paypal_payment(self, request, pk=None):
        # Kiểm tra người dùng đã đăng nhập chưa
        if not request.user.is_authenticated:
            return Response({"detail": "Authentication required."}, status=status.HTTP_401_UNAUTHORIZED)

        # Lấy thông tin đơn hàng
        try:
            order = SalesOrder.objects.get(id=pk)
        except SalesOrder.DoesNotExist:
            return Response({"detail": "Order not found."}, status=status.HTTP_404_NOT_FOUND)

        # Kiểm tra vai trò của người dùng (client hoặc không chứa client)
        user_client = request.user.client
        if user_client is None and 'client' not in [role.name for role in request.user.groups.all()]:
            return Response({"detail": "You are not authorized to make a payment for this order."}, status=status.HTTP_403_FORBIDDEN)

        # Tạo thanh toán PayPal
        payment = paypalrestsdk.Payment({
            "intent": "sale",
            "payer": {"payment_method": "paypal"},
            "transactions": [{
                "amount": {
                    "total": str(order.total_amount),
                    "currency": "USD"
                },
                "description": f"Payment for Order {order.order_number}"
            }],
            "redirect_urls": {
                "return_url": request.build_absolute_uri(f"/api/payments/execute/{order.id}/"),
                "cancel_url": request.build_absolute_uri(f"/api/payments/cancel/{order.id}/")
            }
        })

        # Kiểm tra nếu tạo thanh toán thành công
        if payment.create():
            approval_url = next(link.href for link in payment.links if link.rel == "approval_url")
            return Response({"approval_url": approval_url}, status=status.HTTP_201_CREATED)
        else:
            logger.error(f"PayPal payment creation failed: {payment.error}")
            return Response({"detail": "Payment creation failed."}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['get'])
    def execute_paypal_payment(self, request, pk=None):
        try:
            # Lấy đơn hàng và thông tin thanh toán
            order = SalesOrder.objects.get(id=pk)
            payment_id = request.GET.get('paymentId')
            payer_id = request.GET.get('PayerID')

            if not payment_id or not payer_id:
                return Response({"detail": "Payment ID and Payer ID are required."}, status=status.HTTP_400_BAD_REQUEST)

            # Tìm thanh toán từ PayPal
            payment = paypalrestsdk.Payment.find(payment_id)

            # Kiểm tra nếu thanh toán thành công
            if payment.execute({"payer_id": payer_id}):
                with transaction.atomic():
                    Payment.objects.create(
                        client=order.client,
                        order=order,
                        amount=order.total_amount,
                        payment_method="paypal",
                        status="succeeded",
                        transaction_id=payment.id
                    )
                    order.status = "paid"
                    order.save()

                return Response({"detail": "Payment completed successfully."}, status=status.HTTP_200_OK)
            else:
                return Response({"detail": "Payment execution failed."}, status=status.HTTP_400_BAD_REQUEST)

        except SalesOrder.DoesNotExist:
            return Response({"detail": "Order not found."}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=True, methods=['get'])
    def cancel_paypal_payment(self, request, pk=None):
        try:
            order = SalesOrder.objects.get(id=pk)
            order.status = "cancelled"
            order.save()
            return Response({"detail": "Payment was cancelled."}, status=status.HTTP_200_OK)
        except SalesOrder.DoesNotExist:
            return Response({"detail": "Order not found."}, status=status.HTTP_404_NOT_FOUND)
