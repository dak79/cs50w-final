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
    imageURL = models.URLField(null=True, blank=True)
    description = models.TextField()
    serving = models.CharField(max_length=255, default="4 people")
    preparation_time = models.CharField(max_length=10)
    cooking_time = models.CharField(max_length=10)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"


class Preparation(models.Model):
    """ Preparation steps model """
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE,
                               related_name="instruction"
                               )
    step = models.TextField()


class Quantity(models.Model):
    """ Quantity model """
    quantity = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.quantity}"


class Ingredient(models.Model):
    """ Ingredient model """
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"


class LookupIngRecQty(models.Model):
    """ Lookup Quantity - Ingredient - Recipe """
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE,
                               related_name="ingredients"
                               )
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE,
                                   related_name="recipes"
                                   )
    quantity = models.ForeignKey(Quantity, on_delete=models.CASCADE,
                                 related_name="quantities"
                                 )

    def __str__(self):
        return f"{self.ingredient} qty: {self.quantity} in {self.recipe}"
