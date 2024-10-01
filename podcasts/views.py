from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

def create_podcast(request:HttpRequest) -> HttpResponse:
    return render(request,'podcasts/create_podcast.html')

def podcasts_list(request:HttpRequest) -> HttpResponse:
    return render(request,'podcasts/podcasts_list.html')

def favorite_podcasts(request:HttpRequest) -> HttpResponse:
    return render(request,'podcasts/favorite_podcasts.html')

