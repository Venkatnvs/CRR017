from django.shortcuts import render
from django.http import JsonResponse
from .models import Song

def Main(request):
    return render(request,"index.html")

def get_song_list(request):
    songs = Song.objects.all()
    song_list = [{'name': song.name, 'artist': song.artist, 'img': str(song.img), 'src': str(song.src)} for song in songs]
    return JsonResponse({'songs': song_list})
