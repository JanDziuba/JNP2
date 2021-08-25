from django.db import models


class Offer(models.Model):
    title = models.CharField(max_length=20)
    size = models.DecimalField(max_digits=20, decimal_places=2)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    description = models.CharField(max_length=200)
    seller_username = models.CharField(max_length=20)
    seller_id = models.IntegerField()
