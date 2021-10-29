from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError

from .forms import RegisterForm, LoginForm


def index(request):
    return render(request, "recipes/index.html")


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            mail = form.cleaned_data["mail"]

            # Password matches confirmation
            password = form.cleaned_data["password"]
            confirmation = form.cleaned_data["confirmation"]

            if password != confirmation:
                # AGGIUNGI UN MESSAGGIO DI ERRORE
                return redirect("register")
            
            # Create a new user
            try:
                user = User.objects.create_user(username, email, password)
                user.save()
            except IntegrityError:
                # AGGIUNGI UN MESSAGGIO DI ERRORE (mail o User già presi)
                return redirect("register")
            login(request, user)
            return redirect("index")
    else:
        context = {
            "register_form": RegisterForm()
        }

        return render(request, "recipes/register.html", context)


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form,cleaned_data["password"]
            user = authenticate(request, username=username, password=password)

            # If authentication is successful
            if user is not None:
                login(request, user)
                return redirect("index")
            else:
                # MESSAGGIO (Invalid user/password)
                return redirect("login")
    else:
        context = {
            "login_form": LoginForm()
        }
        
        return render(request, "recipes/login.html", context)


def logout_view(request):
    logout(request)
    return redirect("index")
