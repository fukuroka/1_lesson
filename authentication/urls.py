from django.urls import path
from authentication.views import login,signup,profile

app_name = "authentication"

urlpatterns = [
    path('login/',login,name='login'),
    path('signup/',signup,name='signup'),
    path('profile/',profile,name='profile'),
]