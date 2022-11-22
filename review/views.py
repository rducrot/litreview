from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from . import forms, models


@login_required
def home(request):
    tickets = models.Ticket.objects.all()
    context = {
        'tickets': tickets,
    }
    return render(request, 'review/home.html',
                  context)


@login_required
def ticket_create(request):
    form = forms.TicketForm()
    if request.method == 'POST':
        form = forms.TicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            return redirect('home')
    return render(request, 'review/ticket_create.html',
                  context={'form': form})
