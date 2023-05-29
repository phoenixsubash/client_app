from django import forms


class BootstrapFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.widget = forms.ClearableFileInput(
            attrs={'class': 'form-control-file'})
