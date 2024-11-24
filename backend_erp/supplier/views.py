from rest_framework import viewsets

from backend_erp.permission import IsAuthenticatedWithJWT, TokenMatchesOASRequirements
from .models import Suppliers, Representative, BankingDetail
from .serializers import SupplierSerializer, RepresentativeSerializer, BankingDetailSerializer

class BankingDetailViewSet(viewsets.ModelViewSet):
    queryset = BankingDetail.objects.all()
    serializer_class = BankingDetailSerializer
    permission_classes = [IsAuthenticatedWithJWT, TokenMatchesOASRequirements]
    required_alternate_scopes = {
        "GET": [["read"]],
        "POST": [["create"], ["post", "widget"]],
        "PUT": [["update"], ["put", "widget"]],
        "DELETE": [["delete"], ["scope2", "scope3"]],
    }



class RepresentativeViewSet(viewsets.ModelViewSet):
    queryset = Representative.objects.all()
    serializer_class = RepresentativeSerializer
    permission_classes = [IsAuthenticatedWithJWT, TokenMatchesOASRequirements]
    required_alternate_scopes = {
        "GET": [["read"]],
        "POST": [["create"], ["post", "widget"]],
        "PUT": [["update"], ["put", "widget"]],
        "DELETE": [["delete"], ["scope2", "scope3"]],
    }



class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Suppliers.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = [IsAuthenticatedWithJWT, TokenMatchesOASRequirements]
    required_alternate_scopes = {
        "GET": [["read"]],
        "POST": [["create"], ["post", "widget"]],
        "PUT": [["update"], ["put", "widget"]],
        "DELETE": [["delete"], ["scope2", "scope3"]],
    }

