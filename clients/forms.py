from django import forms
from .models import Client
from cloudinary.forms import CloudinaryFileField


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        profile_image = CloudinaryFileField(
            options={"folder": "profile_images"})
        fields = '__all__'
