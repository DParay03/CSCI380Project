from django import forms
from .models import CheckIn

# Daily CheckinIn Form
class CheckInForm(forms.ModelForm):
    class Meta:
        model = CheckIn
        fields = ['score']

        # Customize form widget for 'score' to use an HTML number input
        widgets = {
            'score': forms.NumberInput(attrs=
                                       {'min': 0,
                                        'max': 10,
                                        'class': 'form-control'
                                        }),
        }