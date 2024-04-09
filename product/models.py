from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    description =models.TextField()
    price =models.DecimalField(max_digits=10,decimal_places =2)
    likes = models.ManyToManyField(User, related_name='liked_products', blank=True)

    def __str__(self):
        return self.name