from itertools import chain

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from . import forms, models


@login_required
def home(request):
    tickets = models.Ticket.objects.all()
    reviews = models.Review.objects.all()
    tickets_and_reviews = sorted(
        chain(tickets, reviews),
        key=lambda instance: instance.time_created,
        reverse=True
    )
    context = {
        'tickets_and_reviews': tickets_and_reviews,
    }
    return render(request, 'review/home.html',
                  context)


@login_required
def user_posts(request):
    tickets = models.Ticket.objects.filter(user=request.user)
    reviews = models.Review.objects.filter(user=request.user)
    tickets_and_reviews = sorted(
        chain(tickets, reviews),
        key=lambda instance: instance.time_created,
        reverse=True
    )
    context = {
        'tickets_and_reviews': tickets_and_reviews,
    }
    return render(request, 'review/user_posts.html',
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


@login_required
def ticket_and_review_create(request):
    ticket_form = forms.TicketForm()
    review_form = forms.ReviewForm()

    if request.method == 'POST':
        ticket_form = forms.TicketForm(request.POST, request.FILES)
        review_form = forms.ReviewForm(request.POST)
        if all([ticket_form.is_valid(), review_form.is_valid()]):
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            review = review_form.save(commit=False)
            review.user = request.user
            review.ticket = ticket
            review.save()
            return redirect('home')
        
    context = {
        'ticket_form': ticket_form,
        'review_form': review_form,
    }
    return render(request, 'review/ticket_and_review_create.html',
                  context=context)


@login_required
def review_create(request, ticket_id):
    ticket = models.Ticket.objects.get(id=ticket_id)
    form = forms.ReviewForm()
    hide_review_button = True

    if request.method == 'POST':
        form = forms.ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.ticket = ticket
            review.save()
            return redirect('home')
    context = {
        'ticket': ticket,
        'form': form,
        'hide_review_button': hide_review_button,
    }
    return render(request, 'review/review_create.html',
                  context=context)
