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
        fields = ['username', 'nickname', 'password']

# class ProfileEditForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput(render_value=True), required=False)

#     class Meta:
#         model = User
#         fields = ['username', 'nickname']
        
#     # def clean(self):
#     #   cleaned_data = super().clean()
#     #   print('Cleaned Data:', cleaned_data)
#     #   return cleaned_data

#     # def clean_password(self):
#     #     password = self.cleaned_data.get('password')
#     #     if password:
#     #         return make_password(password)
#     #     return None
    
#     def save(self, commit=True):
#         user = super().save(commit=False)

#         password = self.cleaned_data.get('password')
#         if password:
#             user.set_password(password)

#         user.nickname = self.cleaned_data.get('nickname')

#         if commit:
#           user.save() # 수정
#         return user