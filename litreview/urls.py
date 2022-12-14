"""litreview URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

import authentication.views
import review.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view(template_name='authentication/login.html',
                               redirect_authenticated_user=True,), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup', authentication.views.signup, name='signup'),
    path('home/', review.views.home, name='home'),
    path('posts/', review.views.user_posts, name='user-posts'),
    path('following/', review.views.following, name='following'),
    path('unfollow/<int:following_id>', review.views.unfollow, name='unfollow'),
    path('ticket/create/', review.views.ticket_create, name='ticket-create'),
    path('ticket/<int:ticket_id>/update/', review.views.ticket_update, name='ticket-update'),
    path('ticket/<int:ticket_id>/delete/', review.views.ticket_delete, name='ticket-delete'),
    path('review/create/', review.views.ticket_and_review_create, name='ticket-and-review-create'),
    path('ticket/<int:ticket_id>/review/create/', review.views.review_create, name='review-create'),
    path('review/<int:review_id>/update/', review.views.review_update, name='review-update'),
    path('review/<int:review_id>/delete/', review.views.review_delete, name='review-delete'),
]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
