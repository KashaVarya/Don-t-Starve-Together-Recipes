from django.db import models


class FoodModel(models.Model):
    name = models.CharField(max_length=32)
    image = models.CharField(max_length=64)
