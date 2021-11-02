from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """ Django User model """
    pass


# Add unique constraint to user.mail field
User._meta.get_field('email')._unique = True


class Recipe(models.Model):
    """ Recipe model """
    name = models.CharField(max_length=255)
    description = models.TextField()
    preparation_time = models.CharField(max_length=10)
    cooking_time = models.CharField(max_length=10)
    date = models.DateField(auto_now_add=True)


class Preparation(models.Model):
    """ Preparation steps model """
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE,
                               related_name="instruction"
                               )
    step = models.TextField()


class Ingredient(models.Model):
    """ Ingredient model """
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE,
                               related_name="ingredient"
                               )
    name = models.CharField(max_length=255)
    quantity = models.CharField(max_length=255)
