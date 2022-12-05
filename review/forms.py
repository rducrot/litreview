from django import forms
from django.db.models import Q
from django.shortcuts import get_object_or_404

from authentication.models import User
from . import models


class TicketForm(forms.ModelForm):
    class Meta:
        model = models.Ticket
        fields = ['title', 'description', 'image']


class ReviewForm(forms.ModelForm):

    class Meta:
        model = models.Review
        fields = ['headline', 'rating', 'body']
        choices = (
            ('0', 0), ('1', 1), ('2', 2),
            ('3', 3), ('4', 4), ('5', 5),
        )
        widgets = {'rating': forms.RadioSelect(choices=choices)}


class UserFollowsForm(forms.ModelForm):
    def __init__(self, user, data=None, *args, **kwargs):
        if data is not None:
            # Data must be mutable
            data = data.copy()
            user_to_follow = get_object_or_404(User, username=data['followed_user'])
            if data['followed_user']:
                data['followed_user'] = user_to_follow.id

        super().__init__(data=data, *args, **kwargs)
        # ensures we can only select other users we don't already follow
        self.choices = User.objects.all().exclude(
            Q(followed_by__in=user.following.all()) |
            Q(id=user.id)
        ).values('username')
        self.fields['followed_user'].widget = forms.TextInput(attrs={'list': 'followed_users'})


    class Meta:
        model = models.UserFollows
        fields = ['followed_user']
