from itertools import chain

from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404

from . import forms, models


@login_required
def home(request):
    user_follows = models.UserFollows.objects.filter(user=request.user).values('followed_user')
    tickets = models.Ticket.objects.filter(
        Q(user__in=user_follows) | Q(user=request.user)
    )
    reviews = models.Review.objects.filter(
        Q(user__in=user_follows) | Q(user=request.user)
    )
    tickets_and_reviews = sorted(
        chain(tickets, reviews),
        key=lambda instance: instance.time_created,
        reverse=True
    )
    home_page = True
    context = {
        'tickets_and_reviews': tickets_and_reviews,
        'home_page': home_page,
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
    post_page = True
    context = {
        'tickets_and_reviews': tickets_and_reviews,
        'post_page': post_page,
    }
    return render(request, 'review/user_posts.html',
                  context)


@login_required
def following(request):
    form = forms.UserFollowsForm()
    followed_users = models.UserFollows.objects.filter(user=request.user)
    following_users = models.UserFollows.objects.filter(followed_user=request.user)
    if request.method == 'POST':
        form = forms.UserFollowsForm(request.POST)
        if form.is_valid():
            user_follows = form.save(commit=False)
            user_follows.user = request.user
            user_follows.save()
            return redirect('following')
    context = {
        'form': form,
        'followed_users': followed_users,
        'following_users': following_users,
    }
    return render(request, 'review/following.html',
                  context=context)


@login_required
def unfollow(request, following_id):
    user_follows = get_object_or_404(models.UserFollows, id=following_id)
    user_follows.delete()
    return redirect('following')


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
def ticket_update(request, ticket_id):
    ticket = get_object_or_404(models.Ticket, id=ticket_id)
    form = forms.TicketForm(instance=ticket)
    if request.method == 'POST':
        form = forms.TicketForm(request.POST, request.FILES, instance=ticket)
        if form.is_valid():
            form.save()
            return redirect('user-posts')
    return render(request, 'review/ticket_update.html',
                  context={'form': form})


@login_required
def ticket_delete(request, ticket_id):
    ticket = get_object_or_404(models.Ticket, id=ticket_id)
    # TODO: Confirmation message
    ticket.delete()
    return redirect('user-posts')


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
    }
    return render(request, 'review/review_create.html',
                  context=context)


@login_required
def review_update(request, review_id):
    review = get_object_or_404(models.Review, id=review_id)
    form = forms.ReviewForm(instance=review)

    if request.method == 'POST':
        form = forms.ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('user-posts')
    context = {
        'form': form,
        'review': review,
    }
    return render(request, 'review/review_update.html',
                  context=context)


@login_required
def review_delete(request, review_id):
    review = get_object_or_404(models.Review, id=review_id)
    # TODO: Confirmation message
    review.delete()
    return redirect('user-posts')
