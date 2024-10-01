from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def posts_list(request:HttpRequest) -> HttpResponse:
    return render(request,'blog/posts_list.html')

def post_details(request:HttpRequest) -> HttpResponse:
    return render(request,'blog/post_details.html')

def create_post(request:HttpRequest) -> HttpResponse:
    return render(request,'blog/create_post.html')
