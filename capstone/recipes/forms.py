from django import forms


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
