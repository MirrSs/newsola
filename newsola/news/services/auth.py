from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import login,logout

from django.urls import reverse
from django.http import HttpResponseRedirect

from loguru import logger

from news.forms import UserRegisterForm,UserLoginForm


def user_register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            logger.debug("New user language:"+str(user.language))
            login(request, user)
            messages.success(request,"Success!")
            logger.warning("NEW USER REGISTERED!")
            return HttpResponseRedirect(reverse('general'))
        else:
            messages.error(request,"Error while registering")
    form = UserRegisterForm()
    return render(request,'news/register.html',{"form":form})

def user_sign(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return HttpResponseRedirect(reverse('general'))
    form = UserLoginForm()
    return render(request,"news/sign.html",{"form":form})

def user_signout(request):
    logout(request)
    return HttpResponseRedirect(reverse('general'))