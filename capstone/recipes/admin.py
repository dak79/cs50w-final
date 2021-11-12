from django.contrib import admin

from .models import User, Recipe, Preparation, Ingredient, Quantity
from .models import LookupIngRecQty, FollowRecipe, CommentRecipe


class UserAdmin(admin.ModelAdmin):
    """ User Admin Model"""

    fields = ("username", "email", "password")
    list_display = ("id", "username", "email", "password")


class RecipeAdmin(admin.ModelAdmin):
    """ User Recipe Model"""

    fields = ("name", "description", "imageURL", "serving",
              "preparation_time", "cooking_time")
    list_display = ("id", "name", "description", "imageURL", "serving",
                    "preparation_time", "cooking_time", "date"
                    )


class IngredientAdmin(admin.ModelAdmin):
    """ Ingredient Admin Model"""

    fields = ("name", )
    list_display = ("id", "name")


class QuantityAdmin(admin.ModelAdmin):
    """ Quantity Admin Model"""

    fields = ("quantity", )
    list_display = ("id", "quantity")


class LookupIngRecQtyAdmin(admin.ModelAdmin):
    """ Lookup Recipe - Ingredient - Quantity Admin Model """

    fields = ("recipe", "ingredient", "quantity")
    list_display = ("id", "recipe", "ingredient", "quantity")


class PreparationAdmin(admin.ModelAdmin):
    """ Preparation Admin Model """

    fields = ("recipe", "num", "imageURL", "step")
    list_display = ("id", "recipe", "num", "imageURL", "step")


class FollowRecipeAdmin(admin.ModelAdmin):
    """ Favorite recipes Admin Model """

    fields = ("user", "recipe")
    list_display = ("id", "user", "recipe")


class CommentAdmin(admin.ModelAdmin):
    """ Comment Admin Model """

    fields = ("user", "recipe", "title", "body", "date")
    list_display = ("id", "user", "recipe", "title", "body", "date")


# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Quantity, QuantityAdmin)
admin.site.register(LookupIngRecQty, LookupIngRecQtyAdmin)
admin.site.register(Preparation, PreparationAdmin)
admin.site.register(FollowRecipe, FollowRecipeAdmin)
admin.site.register(CommentRecipe, CommentAdmin)
