from rest_framework import serializers
from .models import Payment

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['order', 'amount', 'payment_method', 'status', 'transaction_id']

    def create(self, validated_data):
        # Lấy người dùng hiện tại từ request
        user = self.context['request'].user
        # Gán người dùng hiện tại làm client
        validated_data['client'] = user
        return super().create(validated_data)
