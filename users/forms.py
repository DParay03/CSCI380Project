from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegistrationForm(UserCreationForm): # Subclass of UserCreationForm
    email = forms.EmailField()
    first_name = forms.CharField(max_length=30, required=True, help_text='Required')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required')

    class Meta: # Configure the form and relationship to model
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm): # Parameter automatically generates forms tied to a Django model, automatically generating form fields based on model's fields, performs automatic validation
    email = forms.EmailField() # manually adds an email form

    class Meta: #Same as above
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']