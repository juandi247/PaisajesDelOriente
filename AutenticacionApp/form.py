# forms.py
from django import forms
from django.contrib.auth.models import User

# Formulario para el registro (signup)
class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

        

class LoginForm(forms.Form):
    email = forms.EmailField(max_length=100)  # Cambiado a email en lugar de username
    password = forms.CharField(widget=forms.PasswordInput)