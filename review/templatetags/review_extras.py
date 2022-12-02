from django import template

register = template.Library()


@register.filter
def model_type(value):
    return type(value).__name__


@register.filter
def format_date(time_created):
    return f'{time_created.strftime("%H:%m, %d %B %Y")}'


@register.filter
def show_rating(rating):
    stars = ''
    for i in range(rating):
        stars += '★'
    for i in range(5 - rating):
        stars += '☆'
    return stars


@register.simple_tag(takes_context=True)
def get_poster_display(context, user):
    if user == context['user']:
        return 'Vous'
    return user.username


@register.simple_tag(takes_context=True)
def get_ticket_poster_display(context, user):
    if user == context['user']:
        return 'Vous avez demandé une critique.'
    return f'{user.username} a demandé une critique.'


@register.simple_tag(takes_context=True)
def get_review_poster_display(context, user):
    if user == context['user']:
        return 'Vous avez publié une critique.'
    return f'{user.username} a publié une critique.'
