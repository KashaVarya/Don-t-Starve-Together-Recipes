from django.db import models


class DLCModel(models.Model):
    name = models.CharField(max_length=64)
    image = models.CharField(max_length=256)


class IngredientModel(models.Model):
    name = models.CharField(max_length=32)
    image = models.CharField(max_length=256)


class FoodModel(models.Model):
    name = models.CharField(max_length=32)
    image = models.CharField(max_length=256)
    dlc = models.ForeignKey(
        DLCModel,
        on_delete=models.CASCADE
    )
    health = models.IntegerField()
    hunger = models.IntegerField()
    sanity = models.IntegerField()
    perish_time = models.IntegerField()  # days
    cook_time = models.IntegerField()  # seconds
    priority = models.IntegerField()
    ingredients = models.ManyToManyField(
        IngredientModel,
        through='RecipeModel'
    )


class RecipeModel(models.Model):

    RESTRICTION_TYPE = (
        ('no', 'No'),
        ('only', 'Only'),
        ('max', 'Maximum'),
        ('cook', 'Cooked in'),
        ('less=', '<='),
        ('less', '<'),
    )

    ingredient = models.ForeignKey(
        IngredientModel,
        on_delete=models.CASCADE
    )
    food = models.ForeignKey(
        FoodModel,
        on_delete=models.CASCADE
    )
    req_coefficient = models.FloatField()
    restriction_type = models.IntegerField(choices=RESTRICTION_TYPE)
