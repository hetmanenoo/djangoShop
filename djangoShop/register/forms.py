from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(label='Email')
    class Meta(UserCreationForm.Meta):
        model = Register
        fields = ('username', 'email', 'password1', 'password2')