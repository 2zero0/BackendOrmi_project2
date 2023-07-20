from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth.forms import PasswordChangeForm
from django import forms
from .models import User
from django.contrib.auth.forms import UserChangeForm

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'nickname', 'password1', 'password2', 'profile_img']

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class ProfileEditForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['nickname', 'profile_img']