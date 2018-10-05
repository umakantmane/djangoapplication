from django import forms
from django.contrib.auth.forms import UserCreationForm


class SignupUser(UserCreationForm):

    email = forms.EmailField()

class LoginForm(forms.Form):

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)