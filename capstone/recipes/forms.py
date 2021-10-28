from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField(label="Username", max_length=100, min_length=6, 
                               widget=forms.TextInput(attrs={
                                   
                                   "class": "form-item"
                                }))
    mail = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={
                                
                                "class": "form-item"
                            }))
    password = forms.CharField(label="Password", max_length=100, min_length=6,
                               widget=forms.PasswordInput(attrs={
                                   
                                   "class": "form-item"
                                }))
    confirm_password = forms.CharField(label="Confirm Password", max_length=100, min_length=6,
                                       widget=forms.PasswordInput(attrs={
                                           
                                           "class": "form-item"
                                        }))
