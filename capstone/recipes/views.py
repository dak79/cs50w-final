from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordResetForm
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib import messages 
from django.db import IntegrityError

from .forms import RegisterForm, LoginForm
from .models import User


def index(request):
    ''' Homepage '''
    return render(request, "recipes/index.html")


def register(request):
    ''' Register '''
    if request.method == "POST":
        form = RegisterForm(request.POST)

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
                messages.error(request, "Username or Email allready registered")
                return redirect("register")
            login(request, user)
            return redirect("index")
    else:
        if request.user.is_authenticated:
            logout(request)

        context = {
            "register_form": RegisterForm()
        }

        return render(request, "recipes/register.html", context)


def login_view(request):
    ''' Login '''
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)

            # If authentication is successful
            if user is not None:
                login(request, user)
                messages.success(request, "Successfully logged in")
                return redirect("index")
            else:
                messages.error(request, "Invalid Username e/o Password")
                return redirect("login")
    else:
        
        if request.user.is_authenticated:
            logout(request)

        context = {
            "login_form": LoginForm()
        }
        
        return render(request, "recipes/login.html", context)

@login_required(login_url="login")
def logout_view(request):
    ''' Logout '''
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect("index")


def password_reset_request(request):
    ''' Reset password via mail (terminal)'''
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
                    email_template_name = "recipes/password/password_reset_mail.txt"
                    header = {
                        "email": user.email,
                        "domain": "127.0.0.1:8000",
                        "site_name": "Recipes",
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        "token": default_token_generator.make_token(user),
                        "protocol": "http"
                    }

                    email = render_to_string(email_template_name, header)
                    try: 
                        send_mail(subject, email, 'admin@example.com' , [user.email], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse("Invalid header found.")
                    messages.success(request, 'A message with reset password instructions has been sent to your inbox.')
                    return redirect ("index")
            else:
                messages.error(request, "Email does not exist.")
        else:
            messages.error(request, "Invalid Email.")
    else:
        if request.user.is_authenticated:
            logout(request)
        
        return render(request, "recipes/password/password_reset.html", {
        "password_reset_form": PasswordResetForm()
        })


