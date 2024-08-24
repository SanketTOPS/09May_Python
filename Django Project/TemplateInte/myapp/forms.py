from django import forms
from .models import *


class contactForm(forms.ModelForm):
    class Meta:
        model=contct
        fields='__all__'