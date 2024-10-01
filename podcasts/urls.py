from django.urls import path
from podcasts.views import create_podcast,podcasts_list,favorite_podcasts

app_name = "podcasts"

urlpatterns = [
    path('',podcasts_list, name = 'podcasts_list'),
    path('create/',create_podcast, name = 'create_podcast'),
    path('favorite/',favorite_podcasts, name = 'favorite_podcasts'),
]