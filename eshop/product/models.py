from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.TextChoices):
    ELECTRONICS = 'Electronics'
    HOME = 'Home'
    FOOD = 'Food'
    ART = 'Art'
    KITCHEN = 'Kitchen'
    LAPTOPS = 'Laptops'
class Product(models.Model):
    name = models.CharField(max_length=200, default='', blank=False)
    description = models.TextField(max_length=1000, default='', blank=False)
    price = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    brand = models.CharField(max_length=200, default=200, blank=False)
    category = models.CharField(max_length=30, choices=Category.choices)
    ratings = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    stock = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    createdAt = models.TimeField(auto_now_add=True)
