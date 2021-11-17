from django.urls import path

from . import views

urlpatterns = [

    # Views
    path("", views.index, name="index"),
    path("register", views.register, name="register"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("password_reset", views.password_reset_request, name="password_reset"),
    path("user", views.user, name="user"),
    path("favorites", views.favorites, name="favorites"),

    # API Endpoints
    path("api/v1/recipe/ingredients/<int:id>",
         views.ingredients, name="recipe"),
    path("api/v1/recipe/preparation/<int:id>",
         views.preparation, name="preparation"),
    path("api/v1/recipe/follow", views.follow, name="follow"),
    path("api/v1/recipe/comment", views.comment, name="comment"),
    path("api/v1/recipe/edit_comment/<int:id>",
         views.edit_comment, name="edit_comment"),
    path("api/v1/recipe/shopping_list",
         views.shopping_list, name="shopping_list"),
    path("api/v1/recipe/shopping_list_recipe/<int:id>",
         views.shopping_list_recipe, name="shopping_list_recipe")
]
