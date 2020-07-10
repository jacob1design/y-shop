from django.db import models
import uuid
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=200)

class Product(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    created_at = models.DateTimeField(auto_now=True)
    last_modification = models.DateTimeField(auto_now_add=True)
    cover = models.ImageField(null=True)
    category = models.ForeignKey(Category, models.PROTECT)

    def __str__(self):
        return self.name + '( ' + str(self.price) + ')'


class Order(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True)
    user = models.ForeignKey(User, models.CASCADE, related_name='orders')
    date = models.DateTimeField(auto_now=True)
    delivery_address = models.CharField(max_length=255)
    phone_number = models.BigIntegerField()
    total = models.DecimalField(max_digits=10,decimal_places=3)
    product = models.ForeignKey(Product, models.CASCADE)