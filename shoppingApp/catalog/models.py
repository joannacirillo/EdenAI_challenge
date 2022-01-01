from django.db import models

class Product(models.Model):
    name = models.CharField('Product Name', max_length=120)
    price = models.FloatField()
    promotion = models.CharField('', max_length=120)
    image = models.CharField('', max_length=200)