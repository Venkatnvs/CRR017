from django.urls import path
from .views import Main,get_song_list

urlpatterns = [
    path('', Main, name='home'),
    path('get_song_list/', get_song_list, name='get_song_list'),
]
