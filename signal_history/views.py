from django.shortcuts import render , redirect
from django.contrib.auth.hashers import make_password
# from django.contrib.auth import user_logged_in,user_logged_out
from django.contrib.auth.models import User
from django.contrib.auth import authenticate ,login,logout
from django.contrib.auth.decorators import login_required
from datetime import datetime
from . models import *
import logging
logger=logging.getLogger('django')



# Create your views here.





# this is the part of register page 
def register(request):
    if request.method == "POST":
        name = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if name and email and password1 and password2:
            if password1 == password2:
                password=make_password(password1)
                user = User(username=name,email=email,password=password )
                user.save()
                return redirect("login_user")


    return render(request , 'register.html')

# this is the part of login page
def login_user(request):
    if request.method == "POST":
        name = request.POST.get('username')
        password = request.POST.get('password1')
        print(name , password)
        user = authenticate(username = name , password =password)
        if user is not None:
            login(request , user)
            
            if user.is_authenticated:
                user_login = authenticate_history( user_name = request.user , recordstype = 'li' , date_time = datetime.now())
                user_login.save()
                logger.info(msg=f'logged in now {user}')
                return redirect('home')
    return render(request , 'login.html')

# this is for logout part when u want to logout the .


def logout_user(request):
    if request.user.is_authenticated:
        user = request.user
        user_logout = authenticate_history( user_name = request.user , recordstype = 'lo' , date_time = datetime.now())
        print(user_logout)
        user_logout.save()
        logger.info(msg=f'logged out  now {user}')
        logout(request)
    return redirect("login_user")


# this is home page after the login enter this page
@login_required(login_url="login_user")
def home(request):
    return render(request , 'home.html')   