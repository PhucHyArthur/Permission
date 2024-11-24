from rest_framework import serializers
from .models import Suppliers, Representative, BankingDetail

class BankingDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankingDetail
        fields = ['id', 'name', 'holder_name', 'bank_name', 'bank_branch', 'bank_number', 'swift_code', 'created_at']


class RepresentativeSerializer(serializers.ModelSerializer):
    bank_account = serializers.PrimaryKeyRelatedField(queryset=BankingDetail.objects.all(), allow_null=True)

    class Meta:
        model = Representative
        fields = ['id', 'bank_account', 'avatar', 'name', 'birth', 'gender', 'tel', 'email', 'position', 'created_at']


class SupplierSerializer(serializers.ModelSerializer):
    bank_account = serializers.PrimaryKeyRelatedField(queryset=BankingDetail.objects.all(), allow_null=True)
    representative_id = serializers.PrimaryKeyRelatedField(queryset=Representative.objects.all(), allow_null=True)

    class Meta:
        model = Suppliers
        fields = ['id', 'bank_account', 'avatar', 'representative_id', 'name', 'address', 'tel', 'email', 'tax_code', 'created_at']
