from django.db import models
from django.urls import reverse
# Create your models here.

class Ingredient(models.Model):
    name = models.CharField()

    def __str__(self):
        return self.name

class Recipe(models.Model):
    name = models.CharField()

    def __str__(self):
        return self.name

class RecipeIngredient(models.Model):
    name = models.CharField()

    ingredient = models.ForeignKey(
        Ingredient,
    )

    recipe = models.ForeignKey(
        Recipe,
    )

    def __str__(self):
        return self.name