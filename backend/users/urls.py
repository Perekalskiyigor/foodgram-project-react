from django.urls import path
from . import views

urlpatterns = [
    path(
        'users/subscriptions/',
        views.FollowListView,
        name='subscriptions'
    ),
    path(
        'users/<int:user_id>/subscribe/',
        views.FollowViewSet,
        name='subscribe'
    )
]
