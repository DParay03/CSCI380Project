from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm

# Create your views here.
def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account successfully created for {username}!')
            return redirect('login')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field.capitalize()}: {error}")
                    form = UserRegistrationForm()
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})
@login_required(login_url='login')
def profile(request):
    return render(request, 'users/profile.html')

