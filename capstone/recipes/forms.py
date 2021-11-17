from django import forms
from .models import User


class RegisterForm(forms.Form):
    """ Register """

    username = forms.CharField(label="Username", max_length=100, min_length=6,
                               widget=forms.TextInput(attrs={
                                   "autofocus": True
                                }))
    email = forms.EmailField(label="Email", widget=forms.EmailInput())
    password = forms.CharField(label="Password", max_length=100, min_length=6,
                               widget=forms.PasswordInput())
    confirmation = forms.CharField(label="Confirm Password", max_length=100,
                                   min_length=6, widget=forms.PasswordInput())


class LoginForm(forms.Form):
    """ Login """

    username = forms.CharField(label="Username", max_length=100, min_length=6,
                               widget=forms.TextInput(attrs={
                                   "autofocus": True,
                                }))
    password = forms.CharField(label="Password", max_length=100, min_length=6,
                               widget=forms.PasswordInput())


class UserForm(forms.Form, forms.ModelForm):
    """ User Form """

    class Meta:
        model = User
        fields = ("username", "email", "image")

    username = forms.CharField(required=False, label="Username", max_length=100,
                               min_length=6,
                               widget=forms.TextInput(attrs={
                                    "autofocus": True,
                                    })
                               )

    email = forms.EmailField(label="Email",
                             widget=forms.EmailInput(), required=False)
    image = forms.ImageField(required=False)
