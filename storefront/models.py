from distutils.command.upload import upload
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Product(models.Model):
    book_title = models.CharField(max_length=30)
    book_desc = models.CharField(max_length=150)
    book_price=models.FloatField()
    book_Image=models.ImageField(upload_to='storefront/images')



