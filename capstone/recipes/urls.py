from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("register", views.register, name="register"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("password_reset", views.password_reset_request, name="password_reset"),
    path("user", views.user, name="user"),
    path("favorite", views.favorite, name="favorite"),
    path("shopping_list", views.shopping_list, name="shopping_list")
]
