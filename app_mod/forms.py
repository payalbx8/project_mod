from django import forms
from .models import contact

class InfoRegistration(forms.ModelForm):
    class Meta:
        model = contact
        fields = ['name','email','phone','desc']