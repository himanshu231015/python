from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
class Customer(models.Model):
    cname = models.CharField(max_length=100)
    cadd = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    unm = models.CharField(max_length=50)
    pw = models.CharField(max_length=50)

class ImageUploader(models.Model):
    photo=models.ImageField(upload_to="Allimage")
    date=models.DateTimeField(default=now)

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="products/")
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)
    session_id = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart {self.id}"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def get_total_price(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"