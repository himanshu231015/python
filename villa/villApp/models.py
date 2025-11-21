from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Customer(models.Model):
    cname = models.CharField(max_length=100)
    cadd = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    unm = models.CharField(max_length=50)
    pw = models.CharField(max_length=50)