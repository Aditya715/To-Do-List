"""
    Using Django UserCreationForm just because the requirement was of just username and password.
    Not mentioned email id that's why not creating a child of this class.
"""

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


def register(request):
    """
        Register views.
    """

    # checking whether the form is submitted or not
    if request.method == 'POST':
        # Form submission --> True
        form = UserCreationForm(request.POST)
        # check whether the form is valid o not
        if form.is_valid():
            # Getting username for the message
            username = form.cleaned_data.get('username')
            form.save()     # saving user
            messages.success(request, f'Welcome {username}! Your account has been created. Login with your credentials.')
            return redirect('login')
    else:
        form = UserCreationForm()
        
    return render(request, 'registration/register.html', {'form' : form})