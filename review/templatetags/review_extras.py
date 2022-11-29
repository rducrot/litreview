from django import template

register = template.Library()


@register.filter
def model_type(value):
    return type(value).__name__


@register.filter
def show_rating(rating):
    stars = ''
    for i in range(rating):
        stars += '★'
    for i in range(5 - rating):
        stars += '☆'
    return stars
