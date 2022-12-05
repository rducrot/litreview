from django import template

register = template.Library()


@register.filter
def model_type(value):
    """
    Return the type of the model.
    """
    return type(value).__name__


@register.filter
def format_date(time_created):
    """
    Return a formatted date.
    """
    return f'{time_created.strftime("%H:%m, %d %B %Y")}'


@register.filter
def show_rating(rating):
    """
    Return a string composed of stars depending on the rating.
    """
    stars = ''
    for i in range(rating):
        stars += '★'
    for i in range(5 - rating):
        stars += '☆'
    return stars


@register.simple_tag(takes_context=True)
def get_poster_display(context, user):
    """
     Return a name to display depending on the current user.
    """
    if user == context['user']:
        return 'Vous'
    return user.username


@register.simple_tag(takes_context=True)
def get_ticket_poster_display(context, user):
    """
    Return the ticket poster to display depending on the current user.
    """
    if user == context['user']:
        return 'Vous avez demandé une critique.'
    return f'{user.username} a demandé une critique.'


@register.simple_tag(takes_context=True)
def get_review_poster_display(context, user):
    """
     Return the review poster to display depending on the current user.
    """
    if user == context['user']:
        return 'Vous avez publié une critique.'
    return f'{user.username} a publié une critique.'


@register.simple_tag(takes_context=True)
def get_reviewed_by_user(context, ticket):
    """
    Return True if the user already posted a review to the ticket.
    """
    return ticket.review_set.filter(user=context['user']).exists()
