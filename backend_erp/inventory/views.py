from rest_framework import viewsets

from backend_erp.permission import IsAuthenticatedWithJWT, TokenMatchesOASRequirements
from .models import Warehouse, Zone, Rack, Location, RawMaterials, FinishedProducts
from .serializers import WarehouseSerializer, ZoneSerializer, RackSerializer, LocationSerializer, RawMaterialsSerializer, FinishedProductsSerializer


class WarehouseViewSet(viewsets.ModelViewSet):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer
    permission_classes = [IsAuthenticatedWithJWT, TokenMatchesOASRequirements]
    required_alternate_scopes = {
        "GET": [["read"]],
        "POST": [["create"], ["post", "widget"]],
        "PUT": [["update"], ["put", "widget"]],
        "DELETE": [["delete"], ["scope2", "scope3"]],
    }


class ZoneViewSet(viewsets.ModelViewSet):
    queryset = Zone.objects.all()
    serializer_class = ZoneSerializer
    permission_classes = [IsAuthenticatedWithJWT, TokenMatchesOASRequirements]
    required_alternate_scopes = {
        "GET": [["read"]],
        "POST": [["create"], ["post", "widget"]],
        "PUT": [["update"], ["put", "widget"]],
        "DELETE": [["delete"], ["scope2", "scope3"]],
    }


class RackViewSet(viewsets.ModelViewSet):
    queryset = Rack.objects.all()
    serializer_class = RackSerializer
    permission_classes = [IsAuthenticatedWithJWT, TokenMatchesOASRequirements]
    required_alternate_scopes = {
        "GET": [["read"]],
        "POST": [["create"], ["post", "widget"]],
        "PUT": [["update"], ["put", "widget"]],
        "DELETE": [["delete"], ["scope2", "scope3"]],
    }


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [IsAuthenticatedWithJWT, TokenMatchesOASRequirements]
    required_alternate_scopes = {
        "GET": [["read"]],
        "POST": [["create"], ["post", "widget"]],
        "PUT": [["update"], ["put", "widget"]],
        "DELETE": [["delete"], ["scope2", "scope3"]],
    }

class RawMaterialsViewSet(viewsets.ModelViewSet):
    queryset = RawMaterials.objects.all()
    serializer_class = RawMaterialsSerializer
    permission_classes = [IsAuthenticatedWithJWT, TokenMatchesOASRequirements]
    required_alternate_scopes = {
        "GET": [["read"]],
        "POST": [["create"], ["post", "widget"]],
        "PUT": [["update"], ["put", "widget"]],
        "DELETE": [["delete"], ["scope2", "scope3"]],
    }


class FinishedProductsViewSet(viewsets.ModelViewSet):
    queryset = FinishedProducts.objects.all()
    serializer_class = FinishedProductsSerializer
    permission_classes = [IsAuthenticatedWithJWT]  #TokenMatchesOASRequirements
    # required_alternate_scopes = {
    #     "GET": [["read"]],
    #     "POST": [["create"], ["post", "widget"]],
    #     "PUT": [["update"], ["put", "widget"]],
    #     "DELETE": [["delete"], ["scope2", "scope3"]],
    # }
