from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('', register  , name='register'),
    path('login/',  login_user  ,name='login_user'),
    path('home/', home , name='home'),
    path('logout_user', logout_user , name='logout_user'),  
    
   
]
