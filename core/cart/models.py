from django.db import models
from products.models import Product
from django.contrib.auth.models import User

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    product = models.ManyToManyField(to=Product, blank=True)

    def __str__(self) -> str:
        return f'Корзина: {self.user}'
