from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from users.models import User



class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["email", "password1", "password2"]


class UserLoginForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.EmailInput(attrs={"autofocus": True}))
