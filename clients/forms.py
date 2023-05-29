from django import forms
from .models import Client
from .bootstrap_forms import BootstrapFileField
from django.contrib.auth.models import User


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        profile_image = BootstrapFileField()
        fields = '__all__'


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
