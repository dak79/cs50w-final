from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.db import IntegrityError
from django.db.models.query_utils import Q
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.core.mail import send_mail, BadHeaderError
from django.core.paginator import Paginator
import json

from .forms import RegisterForm, LoginForm, UserForm
from .models import User, Recipe, LookupIngRecQty, Preparation, FollowRecipe
from .models import CommentRecipe, ShoppingList

# VIEWS #


def index(request):
    """ Homepage view - All Recipes """

    # Get all recipes
    recipes_list = Recipe.objects.all()

    # Paginate
    paginator = Paginator(recipes_list, 5)
    page_number = request.GET.get("page", 1)

    # Page object
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj,
        "title": "All Recipes",
    }

    return render(request, "recipes/index.html", context)


def login_view(request):
    """ Login view"""

    if request.method == 'POST':
        form = LoginForm(request.POST)

        # Form validation
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)

            # If authentication is successful
            if user is not None:

                # Log in
                login(request, user)
                messages.success(request, "Successfully logged in")
                return redirect("index")
            else:
                messages.error(request, "Invalid Username e/o Password")
                return redirect("login")
    else:

        if request.user.is_authenticated:

            # Log out authenticated user
            logout(request)

        context = {
            "login_form": LoginForm()
        }

        return render(request, "recipes/login.html", context)


def register(request):
    """ Register view """

    if request.method == "POST":
        form = RegisterForm(request.POST)

        # Form validation
        if form.is_valid():
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]

            # Password matches confirmation
            password = form.cleaned_data["password"]
            confirmation = form.cleaned_data["confirmation"]

            if password != confirmation:
                messages.error(request, 'Passwords must match')
                return redirect("register")

            # Create a new user
            try:
                user = User.objects.create_user(username, email, password)
                user.save()
            except IntegrityError:
                messages.error(
                    request, "Username or Email allready registered")
                return redirect("register")

            # Login
            login(request, user)
            return redirect("index")
    else:
        if request.user.is_authenticated:

            # Log out authenticated user
            logout(request)

        context = {
            "register_form": RegisterForm()
        }

        return render(request, "recipes/register.html", context)


@login_required(login_url="login")
def logout_view(request):
    """ Logout """

    # Log out
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect("index")


@login_required(login_url="login")
def user(request):
    """ User page view """

    form = UserForm(initial={"username": request.user.username,
                             "email": request.user.email,
                             "image": request.user.image
                             })

    if request.method == "POST":
        form = UserForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()

            return redirect("user")

    context = {
        "user_form": form
    }
    return render(request, "recipes/user.html", context)


@login_required(login_url="login")
def favorites(request):
    """ Favorite view """

    # Get the recipes followed by user
    favorites = FollowRecipe.objects.filter(user=request.user).all()
    favorites_list = []

    # Get recipe information
    for favorite in favorites:
        recipe = Recipe.objects.get(pk=favorite.recipe.id)

        # Recipe list
        favorites_list.append(recipe)

    # Paginate
    paginator = Paginator(favorites_list, 5)
    page_number = request.GET.get("page", 1)

    # Page object
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj,
        "title": "Favorites",
    }

    return render(request, "recipes/index.html", context)


def password_reset_request(request):
    """ Reset password via mail (terminal) """

    if request.method == "POST":

        # Get the form
        form = PasswordResetForm(request.POST)

        # Validate the form
        if form.is_valid():
            data = form.cleaned_data["email"]
            users = User.objects.filter(Q(email=data))
            if users.exists():
                for user in users:

                    # Configure and send mail (via terminal)
                    subject = "Password Reset Requested"
                    email_template_name = "recipes/password/reset_mail.txt"

                    header = {
                        "email": user.email,
                        "domain": "127.0.0.1:8000",
                        "site_name": "Recipes",
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        "token": default_token_generator.make_token(user),
                        "protocol": "http"
                    }

                    # Render email
                    email = render_to_string(email_template_name, header)
                    try:

                        # Send email
                        send_mail(subject, email, 'admin@example.com',
                                  [user.email], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse("Invalid header found.")
                    messages.success(
                        request,
                        "A message with reset password instructions has been"
                        "sent to your inbox.")
                    return redirect("index")
            else:
                messages.error(request, "Email does not exist.")
        else:
            messages.error(request, "Invalid Email.")
    else:
        if request.user.is_authenticated:

            # Log out authenticated user
            logout(request)

        return render(request, "recipes/password/password_reset.html", {
            "password_reset_form": PasswordResetForm()
        })


# API #


@login_required(login_url="login")
def ingredients(request, id):
    """ API: ingredients for a given recipe (GET)"""

    # Get recipe ingredients
    ingredients = LookupIngRecQty.objects.filter(recipe=id).all()

    return JsonResponse([ingredient.serialize() for ingredient in ingredients],
                        safe=False)


@login_required(login_url="login")
def preparation(request, id):
    """ API: preparation steps for a given recipe (GET) """

    # Get recipe preparation steps
    steps = Preparation.objects.filter(recipe=id).all().order_by("num")

    return JsonResponse([step.serialize() for step in steps],
                        safe=False)


@login_required(login_url="login")
def follow(request):
    """
    API:
    add favorite (POST),
    remove favorite (DELETE),
    get favorite (GET)
    """

    # Add a recipe to favorite
    if request.method == 'POST':
        data = json.loads(request.body)

        favorite = FollowRecipe(
            recipe_id=int(data["recipe"]),
            user_id=int(data["user"]))
        favorite.save()
        return JsonResponse({"message": "Added to favorite"})

    # Delete a recipe from favorite
    elif request.method == 'DELETE':
        data = json.loads(request.body)
        favorite = FollowRecipe.objects.filter(recipe=data['id']).first()
        favorite.delete()
        return JsonResponse({"message": "Deleted from favorite"})

    else:

        # Get the favorite recipes
        favorites = FollowRecipe.objects.filter(user=request.user.id).all()
        return JsonResponse([favorite.serialize() for favorite in favorites],
                            safe=False)


@login_required(login_url="login")
def comment(request):
    """ API: add comment(POST) and get all comments (GET) """

    # Add comment
    if request.method == 'POST':
        data = json.loads(request.body)
        comment = CommentRecipe(user_id=data["user"],
                                recipe_id=data["recipe"],
                                title=data["title"],
                                body=data["body"])
        comment.save()

        return JsonResponse({"message": "Comment added"})

    # Get comments
    comments = CommentRecipe.objects.all().order_by("-date")

    return JsonResponse([comment.serialize() for comment in comments],
                        safe=False)


@login_required(login_url="login")
def edit_comment(request, id):
    """
    API:
    get a comment(GET),
    edit a comment (PUT),
    delete a comment(DELETE)
    """

    # Get the comment
    comment = CommentRecipe.objects.get(pk=id)

    # Edit comment
    if request.method == "PUT":

        data = json.loads(request.body)
        comment.body = data["body"]
        comment.save()

        return JsonResponse({"message": "Comment successfully updated"})

    # Delete comment
    if request.method == "DELETE":
        comment.delete()
        return JsonResponse({"message": "Comment successfully deleted"})

    return JsonResponse(comment.serialize(), safe=False)


@login_required(login_url="login")
def shopping_list(request):
    """
    Shopping List views
    API:
    add recipe ingredients(POST),
    get all recipe ingerdients(GET),
    delete recipe ingredients(DELETE)
    """

    # Add recipe to shopping list
    if request.method == 'POST':
        data = json.loads(request.body)

        recipe = ShoppingList(user_id=data["user"],
                              recipe_id=data["recipe"])
        recipe.save()

        return JsonResponse({"message": "Recipes added to shopping list"})

    # Delete recipe from shopping list
    if request.method == 'DELETE':
        data = json.loads(request.body)

        recipe = ShoppingList.objects.get(pk=int(data["id"]))
        recipe.delete()

        return JsonResponse({"message": "Deleted from shopping list"})

    # Get all ingredients and recipes in shopping list
    recipes = ShoppingList.objects.filter(user=request.user).all()

    ingredient_list = []

    for recipe in recipes:
        ingredients = LookupIngRecQty.objects.filter(
            recipe=recipe.recipe.id).all()
        ingredient_list.append(ingredients)

    context = {
        "recipes": recipes,
        "ingredients": list(ingredient_list)
    }

    return render(request, "recipes/shopping_list.html", context)


@login_required(login_url="login")
def shopping_list_recipe(request, id):
    """
    API:
    Find recipe in shopping list (GET),
    delete recipe from shopping list (DELETE)
    """

    # Get recipe in shopping list
    recipe = ShoppingList.objects.filter(user=request.user,
                                         recipe=id).first()

    if request.method == 'DELETE':
        recipe.delete()

        return JsonResponse({"message": "Deleted from shopping list"})

    try:
        data = recipe.serialize()
    except AttributeError:
        data = False
    return JsonResponse(data, safe=False)
