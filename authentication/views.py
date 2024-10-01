from django.http import HttpRequest, HttpResponse
from django.shortcuts import render



def login(request:HttpRequest) -> HttpResponse:
    return render(request, 'authentication/login.html')

def signup(request:HttpRequest) -> HttpResponse:
    return render(request, 'authentication/signup.html')

def profile(request:HttpRequest) ->HttpResponse:
    return render(request, 'authentication/profile.html')