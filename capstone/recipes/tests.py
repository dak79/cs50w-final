from django.test import TestCase

from .models import Recipe, Preparation, Ingredient


# Test database
class RecipeTest(TestCase):
    """ Test for models: Recipe, Preparation and Ingredient """

    def setUp(self):

        # Create recipe
        r1 = Recipe(name="Aglio, olio e peperoncino",
                    description="Fresh and rustic pasta",
                    preparation_time="15m",
                    cooking_time="9m",
                    )
        r1.save()

        # Create ingredients
        rec1 = Recipe.objects.get(pk=1)
        i1 = Ingredient(
                name="Garlic",
                quantity="1 clove"
            )
        i1.save()
        i1.recipe.add(rec1)

        i2 = Ingredient(
                name="Extra virgin oil",
                quantity="50ml"
            )
        i2.save()
        i2.recipe.add(rec1)

        i3 = Ingredient(
                name="Chili pepper",
                quantity="1"
            )
        i3.save()
        i3.recipe.add(rec1)

        i4 = Ingredient(
                name="Spaghetti",
                quantity="100g"
            )
        i4.save()
        i4.recipe.add(rec1)

        i5 = Ingredient(
                name="Salt",
                quantity="qb"
            )
        i5.save()
        i5.recipe.add(rec1)

        # Create preparation steps
        rp1 = Recipe.objects.get(pk=1)

        s1 = Preparation(recipe=rp1, step="Clean garlic"
                         " and chili pepper."
                         )
        s1.save()

        s2 = Preparation(recipe=rp1, step="Cut garlic and chili pepper"
                         " in small and tiny pieces."
                         )
        s2.save()

        s3 = Preparation(recipe=rp1, step="Put oil in a small pan")
        s3.save()

        s4 = Preparation(recipe=rp1, step="Add garlic and chili pepper"
                         " to oil in the pan."
                         )
        s4.save()

        s5 = Preparation(recipe=rp1, step="Cook the souce in low fire")
        s5.save()

        s6 = Preparation(recipe=rp1, step="When garlic start to be"
                         " little bit brown, close the fire."
                         )
        s6.save()

        s7 = Preparation(recipe=rp1, step="Fullfil a pot with water")
        s7.save()

        s8 = Preparation(recipe=rp1, step="When water is boiling put"
                         " rock salt."
                         )
        s8.save()

        s9 = Preparation(recipe=rp1, step="When salt is dissolved put"
                         " spaghetti and cook them for 9m."
                         )
        s9.save()

        s10 = Preparation(recipe=rp1, step="Drain spaghetti, add souce, "
                          " mix and enjoy."
                          )
        s10.save()

    def test_recipe_count(self):
        """ Recipe saved in db should be 1"""
        r = Recipe.objects.all()

        self.assertEqual(r.count(), 1)

    def test_ingredient_count(self):
        """ Ingredients saved in db should be 5"""
        i = Ingredient.objects.all()

        self.assertEqual(i.count(), 5)

    def test_step_count(self):
        """ Steps saved in db should be 10 """
        s = Preparation.objects.all()

        self.assertEqual(s.count(), 10)
