from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.postgres.fields import ArrayField

class Warehouse(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    capacity = models.IntegerField(default=0)
    description = models.CharField(max_length=255)
    isDelete = models.BooleanField(default=False)
    isFulled = models.BooleanField(_("Is Fulled"), default=True)
    
    def __str__(self):
        return self.name

class Zone(models.Model):
    id = models.AutoField(primary_key=True)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, related_name="zones")
    name = models.CharField(max_length=255)
    capacity = models.IntegerField(default=0)
    description = models.CharField(max_length=255)
    isDelete = models.BooleanField(default=False)
    isFulled = models.BooleanField(_("Is Fulled"), default=True)
    
    def __str__(self):
        return self.name
    
class Aisle(models.Model):
    id = models.AutoField(primary_key=True)
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE, related_name="aisles")
    name = models.CharField(max_length=255)
    capacity = models.IntegerField(default=0)
    description = models.CharField(max_length=255)
    isDelete = models.BooleanField(default=False)
    isFulled = models.BooleanField(_("Is Fulled"), default=True)
    
    def __str__(self):
        return self.name
    
class Rack(models.Model):
    id = models.AutoField(primary_key=True)
    aisle = models.ForeignKey(Aisle, on_delete=models.CASCADE, related_name="racks")
    name = models.CharField(max_length=255)
    capacity = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    isDelete = models.BooleanField(default=False)
    isFulled = models.BooleanField(_("Is Fulled"), default=True)
    
    def __str__(self):
        return self.name

class Location(models.Model):
    id = models.AutoField(primary_key=True)
    rack = models.ForeignKey(Rack, on_delete=models.CASCADE, related_name="locations")
    bin_number = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    quantity = models.IntegerField(default=0)
    isDelete = models.BooleanField(default=False)
    isFulled = models.BooleanField(_("Is Fulled"), default=True)
    
    def __str__(self):
        return self.bin_number

class RawMaterials(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    category = models.CharField(max_length=255)
    image = ArrayField(models.URLField(max_length=200), blank=True, null=True)
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.CharField(max_length=50)
    quantity_in_stock = models.IntegerField(default=0)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name="raw_materials")
    description = models.CharField(max_length=255)
    expired_date = models.DateField(_("Expiry Date"))
    isAvailable = models.BooleanField(_("Is Available"), default=True)
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.name
     
class FinishedProducts(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_in_stock = models.IntegerField(default=0)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name="finished_products")
    description = models.CharField(max_length=255)
    expired_date = models.DateField(_("Expiry Date"))
    main_image = models.CharField(max_length=255)
    sub_image_1 = models.CharField(max_length=255)
    sub_image_2 = models.CharField(max_length=255)
    isAvailable = models.BooleanField(_("Is Available"), default=True)
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.name
