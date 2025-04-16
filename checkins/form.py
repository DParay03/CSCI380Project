from django import forms
from .models import CheckIn

class CheckInForm(forms.ModelForm):
    class Meta:
        model = CheckIn
        fields = ['score']
        widgets = {
            'score': forms.NumberInput(attrs={'min': 0, 'max': 10, 'class': 'form-control'}),
        }