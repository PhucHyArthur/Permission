from django.db import models
from db_diy.models import Clients 
from inventory.models import FinishedProducts 

class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    client = models.ForeignKey(Clients, on_delete=models.CASCADE)

    def __str__(self):
        return f"Cart of Client {self.client.id}"

class CartLine(models.Model):
    id = models.AutoField(primary_key=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_lines')
    product = models.ForeignKey(FinishedProducts, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    unit_price = models.IntegerField()

    def __str__(self):
        return f"Line in Cart {self.cart.id} for Product {self.product.name}"
