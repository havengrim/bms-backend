from django.urls import path
from .views import create_announcement, list_announcements

urlpatterns = [
    path('', list_announcements, name='list_announcements'),
    path('create/', create_announcement, name='create_announcement'),
]
