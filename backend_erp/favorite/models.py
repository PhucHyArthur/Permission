from django.db import models
from db_diy.models import Clients
from inventory.models import FinishedProducts

class Favorites(models.Model):
    id = models.AutoField(primary_key=True)
    client = models.ForeignKey(Clients, on_delete=models.CASCADE)

    def __str__(self):
        return f"Favorites of Client {self.client}"

class FavoriteLine(models.Model):
    id = models.AutoField(primary_key=True)
    favorites = models.ForeignKey(Favorites, on_delete=models.CASCADE, related_name='favorite_lines')
    product = models.ForeignKey(FinishedProducts, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Favorite Line for Product {self.product} in Favorite {self.favorites.id}"
