from django.db import models


class User(models.Model):
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.username

class Product(models.Model):
    title = models.CharField(max_length=20)
    size = models.DecimalField(max_digits=20, decimal_places=2)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    description = models.CharField(max_length=200)
