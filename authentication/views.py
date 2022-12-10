from django.shortcuts import render, redirect

from . import forms


def signup(request):
    """
    Signup page.
    """
    form = forms.SignupForm()
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    return render(request, 'authentication/signup.html',
                  context={'form': form})
