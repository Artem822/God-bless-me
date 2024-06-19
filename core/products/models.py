from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='static/img')
    price = models.IntegerField()
    stock = models.IntegerField()

    def __str__(self):
        return self.name
    