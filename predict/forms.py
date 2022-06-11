from django import forms

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import MyUser


class SignUpForm(UserCreationForm):
    pass

    class Meta:
        model = MyUser
        fields = ('username', 'password1', 'password2', )
