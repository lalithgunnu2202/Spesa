from django.db import models
from django.contrib.auth.models import  User
from home.models import Product

# Create your models here.
class Cart_item(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE )

    def __str__(self):
        return f"{self.product.prod_id} for {self.user} "