from django.test import TestCase
from django.test import Client

from .models import Recipe, Preparation, Ingredient, Quantity, LookupIngRecQty
from .models import User, FollowRecipe, ShoppingList, CommentRecipe


class RecipeModelTest(TestCase):
    """
    Test for models:
    - Recipe,
    - Ingredient,
    - Quantity,
    - Lookup Recipe Ingredient Quantity,
    - Preparation Steps
    - FollowRecipe
    - Shopping List
    """

    def setUp(self):

        # Create recipe
        r1 = Recipe(name="Spaghetti with Tomato Sauce",
                    imageURL="https://www.giallozafferano.com/images/228-22832/"
                             "spaghetti-with-tomato-sauce_1200x800.jpg",
                    description="A symbolic dish of Italian cuisine",
                    serving="4 people",
                    preparation_time="10m",
                    cooking_time="70m",
                    )

        r1.save()

        # Create User
        u1 = User(username="daniele",
                  email="danielecampari@gmail.com",
                  password="12345678")

        u1.save()

        # Create ingredients
        i1 = Ingredient(name="Spaghetti")
        i1.save()

        i2 = Ingredient(name="Extra virgin oil")
        i2.save()

        i3 = Ingredient(name="Basil")
        i3.save()

        i4 = Ingredient(name="Peel Tomatoes")
        i4.save()

        i5 = Ingredient(name="Garlic")
        i5.save()

        i6 = Ingredient(name="Fine Salt")
        i6.save()

        # Create quantities
        q1 = Quantity(quantity="320 g.")
        q1.save()
        q2 = Quantity(quantity="30 g.")
        q2.save()
        q3 = Quantity(quantity="to taste")
        q3.save()
        q4 = Quantity(quantity="800 g.")
        q4.save()
        q5 = Quantity(quantity="1 clove")
        q5.save()

        # Connect recipe, ingredient and quantiies
        r2 = Recipe.objects.get(pk=1)

        i7 = Ingredient.objects.get(pk=1)
        q7 = Quantity.objects.get(pk=1)
        c1 = LookupIngRecQty(
                            recipe=r2,
                            ingredient=i7,
                            quantity=q7
                            )
        c1.save()

        i8 = Ingredient.objects.get(pk=2)
        q8 = Quantity.objects.get(pk=2)
        c2 = LookupIngRecQty(
                            recipe=r2,
                            ingredient=i8,
                            quantity=q8
                            )
        c2.save()

        i9 = Ingredient.objects.get(pk=3)
        q9 = Quantity.objects.get(pk=3)
        c3 = LookupIngRecQty(
                            recipe=r2,
                            ingredient=i9,
                            quantity=q9
                            )
        c3.save()

        i10 = Ingredient.objects.get(pk=4)
        q10 = Quantity.objects.get(pk=4)
        c4 = LookupIngRecQty(
                            recipe=r2,
                            ingredient=i10,
                            quantity=q10
                            )
        c4.save()

        i11 = Ingredient.objects.get(pk=5)
        q11 = Quantity.objects.get(pk=5)
        c5 = LookupIngRecQty(
                            recipe=r2,
                            ingredient=i11,
                            quantity=q11
                            )
        c5.save()

        i12 = Ingredient.objects.get(pk=6)
        c6 = LookupIngRecQty(
                            recipe=r2,
                            ingredient=i12,
                            quantity=q9
                            )
        c6.save()

        # Create preparation steps
        s1 = Preparation(recipe=r2,
                         num=1,
                         imageURL="https://www.giallozafferano.com/images/"
                                  "ricette/228/22832/"
                                  "16513_spaghetti_al_pomodoro_strip_1-3.jpg",
                         step="To make spaghetti with tomato sauce..."
                         )
        s1.save()

        s2 = Preparation(recipe=r2,
                         num=2,
                         imageURL="https://www.giallozafferano.com/images/"
                                  "ricette/228/22832/"
                                  "16513_spaghetti_al_pomodoro_strip_4-6.jpg",
                         step="Cover with a lid and cook..."
                         )
        s2.save()

        s3 = Preparation(recipe=r2,
                         num=3,
                         imageURL="https://www.giallozafferano.com/images/"
                                  "ricette/228/22832/"
                                  "16513_spaghetti_al_pomodoro_strip_7-9.jpg",
                         step="Pour the source back into the pan..."
                         )
        s3.save()
        s4 = Preparation(recipe=r2,
                         num=4,
                         imageURL="https://www.giallozafferano.com/images/"
                                  "ricette/228/22832/"
                                  "16513_spaghetti_al_pomodoro_strip_10-12.jpg",
                         step="Drain the spaghetti al dente..."
                         )
        s4.save()

        # Follow a recipe
        u1 = User.objects.get(pk=1)
        r3 = Recipe.objects.get(pk=1)
        f1 = FollowRecipe(user=u1, recipe=r3)
        f1.save()

        # Put a recipe in shopping list
        u2 = User.objects.get(pk=1)
        r4 = Recipe.objects.get(pk=1)
        sl = ShoppingList(user=u2, recipe=r4)
        sl.save()

        # Create a comment
        u3 = User.objects.get(pk=1)
        r5 = Recipe.objects.get(pk=1)
        c = CommentRecipe(user=u3,
                          recipe=r5,
                          title="Very good",
                          body="Very good recipe, try it!")
        c.save()

    def test_recipe_count(self):
        """ Recipe saved in db should be 1 """

        r = Recipe.objects.all()
        self.assertEqual(r.count(), 1)

    def test_ingredient_count(self):
        """ Ingredients saved in db should be 6 """

        i = Ingredient.objects.all()
        self.assertEqual(i.count(), 6)

    def test_quantity_count(self):
        """ Quantity saved in db shoul be 5 """

        q = Quantity.objects.all()
        self.assertEqual(q.count(), 5)

    def test_lookup_count(self):
        """ LookupIngRecQty instance saved in db should be 6 """

        c = LookupIngRecQty.objects.all()
        self.assertEqual(c.count(), 6)

    def test_step_count(self):
        """ Steps saved in db should be 4 """

        s = Preparation.objects.all()
        self.assertEqual(s.count(), 4)

    def test_recipe_identified(self):
        """ Test if the recipe is correctly identified """

        r = Recipe.objects.get(pk=1)
        self.assertEqual(r.name, "Spaghetti with Tomato Sauce")
        self.assertEqual(
            r.imageURL, "https://www.giallozafferano.com/images/228-22832/"
                        "spaghetti-with-tomato-sauce_1200x800.jpg"
                        )
        self.assertEqual(r.description, "A symbolic dish of Italian cuisine")
        self.assertEqual(r.serving, "4 people")
        self.assertEqual(r.preparation_time, "10m")
        self.assertEqual(r.cooking_time, "70m")

    def test_ingredient_name(self):
        """ Test if the ingredient is correctly identified """

        i = Ingredient.objects.get(pk=5)
        self.assertEqual(i.name, "Garlic")

    def test_quantity_name(self):
        """ Test if the quantity is correctly identified """

        q = Quantity.objects.get(pk=5)
        self.assertEqual(q.quantity, "1 clove")

    def test_lookup_name(self):
        """ Test if the lookup is correctly identified """

        c = LookupIngRecQty.objects.get(pk=5)
        self.assertEqual(c.recipe.name, "Spaghetti with Tomato Sauce")
        self.assertEqual(c.ingredient.name, "Garlic")
        self.assertEqual(c.quantity.quantity, "1 clove")

    def test_preparation_name(self):
        """ Test if preparation step is correctly identified """

        s = Preparation.objects.get(pk=4)
        self.assertEqual(s.recipe.name, "Spaghetti with Tomato Sauce")
        self.assertEqual(s.num, 4)
        self.assertEqual(
            s.imageURL, "https://www.giallozafferano.com/images/ricette/228/"
                        "22832/16513_spaghetti_al_pomodoro_strip_10-12.jpg"
                        )
        self.assertEqual(s.step, "Drain the spaghetti al dente...")

    def test_follow_recipe(self):
        """ Recipe followed should be 1 """

        f = FollowRecipe.objects.filter(pk=1).all()
        self.assertEqual(f.count(), 1)

    def test_shopping_list(self):
        """ Recipe in shopping list should be 1 """

        sl = ShoppingList.objects.filter(pk=1).all()
        self.assertEqual(sl.count(), 1)

    def test_user(self):
        """ User should be 1 """

        u = User.objects.filter(pk=1).all()
        self.assertEqual(u.count(), 1)

    def test_comment(self):
        """
        Comment count should be 1
        Comment title: "Very good"
        Comment body: "Very good recipe, try it!"
        """

        cn = CommentRecipe.objects.filter(pk=1).all()
        co = CommentRecipe.objects.get(pk=1)
        self.assertEqual(cn.count(), 1)
        self.assertEqual(co.title, "Very good")
        self.assertEqual(co.body, "Very good recipe, try it!")


class RoutesTest(TestCase):
    """ Test routes """

    def test_index_route(self):
        """ Status code 200 OK """

        c = Client()
        response = c.get("")
        self.assertEqual(response.status_code, 200)

    def test_register_route(self):
        """ Status code 200 OK """

        c = Client()
        response = c.get("/register")
        self.assertEqual(response.status_code, 200)

    def test_login_route(self):
        """ Status code 200 OK """

        c = Client()
        response = c.get("/login")
        self.assertEqual(response.status_code, 200)

    def test_logout_route(self):
        """ Status code 302 REDIRECT """

        c = Client()
        response = c.get("/logout")
        self.assertEqual(response.status_code, 302)

    def test_password_reset_route(self):
        """ Status code 200 OK """

        c = Client()
        response = c.get("/password_reset")
        self.assertEqual(response.status_code, 200)

    def test_user_route(self):
        """ Status code 302 REDIRECT """

        c = Client()
        response = c.get("/user")
        self.assertEqual(response.status_code, 302)

    def test_favorites_route(self):
        """ Status code 302 REDIRECT """

        c = Client()
        response = c.get("/favorites")
        self.assertEqual(response.status_code, 302)
