from django.shortcuts import render

from . import forms


def signup(request):
    """
    Signup page.
    """
    form = forms.SignupForm()
    return render(request, 'authentication/signup.html',
                  context={'form': form})
