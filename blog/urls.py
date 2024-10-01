from django.urls import path
from blog.views import posts_list,post_details,create_post

app_name = "blog"

urlpatterns = [
    path('posts/',posts_list,name = 'posts'),
    path('details/',post_details, name = 'details'),
    path('create/',create_post, name = 'create_post'),
]