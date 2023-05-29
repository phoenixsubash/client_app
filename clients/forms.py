from django import forms
from .models import Client
# from cloudinary.forms import CloudinaryFileField
from .bootstrap_forms import BootstrapFileField


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        profile_image = BootstrapFileField()
        fields = '__all__'
