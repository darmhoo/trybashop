from django import forms
from . import models

class Login(forms.Form):
    name = forms.CharField
    password = forms.PasswordInput
    class Meta:
        model = models.UserProfile

