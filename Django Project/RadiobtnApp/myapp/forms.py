from django import forms
from .models import *

class signupForm(forms.ModelForm):
    class Meta:
        model = usersignup
        fields = ['firstname', 'lastname', 'username', 'city', 'gender']
        widgets = {
            'gender': forms.RadioSelect,
        }