from rest_framework import viewsets

from backend_erp.permission import IsAuthenticatedWithJWT, TokenMatchesOASRequirements
from .models import PurchasesBill
from .serializers import PurchasesBillSerializer

from .models import SalesBill
from .serializers import SalesBillSerializer

class PurchasesBillViewSet(viewsets.ModelViewSet):
    queryset = PurchasesBill.objects.all()
    serializer_class = PurchasesBillSerializer
    permission_classes = [IsAuthenticatedWithJWT, TokenMatchesOASRequirements]
    required_alternate_scopes = {
        "GET": [["read"]],
        "POST": [["create"], ["post", "widget"]],
        "PUT": [["update"], ["put", "widget"]],
        "DELETE": [["delete"], ["scope2", "scope3"]],
    }


class SalesBillViewSet(viewsets.ModelViewSet):
    queryset = SalesBill.objects.all()
    serializer_class = SalesBillSerializer
    permission_classes = [IsAuthenticatedWithJWT, TokenMatchesOASRequirements]
    required_alternate_scopes = {
        "GET": [["read"]],
        "POST": [["create"], ["post", "widget"]],
        "PUT": [["update"], ["put", "widget"]],
        "DELETE": [["delete"], ["scope2", "scope3"]],
    }
