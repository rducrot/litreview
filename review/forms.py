from django import forms
from django.db.models import Q

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
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # ensures we can only select other users we don't already follow
        self.fields['followed_user'].queryset = User.objects.all().exclude(
            Q(followed_by__in=user.following.all()) |
            Q(id=user.id)
        )

    class Meta:
        model = models.UserFollows
        fields = ['followed_user']
