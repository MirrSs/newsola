from django.shortcuts import render
from loguru import logger
from news.forms import SearchForm
from news.models import Search

from news.services.auth import *
from news.services.news_api import get_headlines,search_news
from django.contrib.auth.decorators import login_required


# Create your views here.

from django.http import HttpResponse

logger.add("debuglog.json", format="{time} {level} {message}", level="WARNING",
 rotation="50 KB",compression="zip",serialize=True)

def index(request,category="general"):
    news_list = get_headlines(request,category)
    context = {'news_list':news_list,'category':category}
    return render(request, 'news/index.html', context)

def general_view(request):
    news_list = get_headlines(request)
    context = {'news_list':news_list}
    return render(request, 'news/index.html', context)

def search_view(request):
    if request.method != 'POST':
        form = SearchForm()
    else:
        form = SearchForm(request.POST)
        if form.is_valid():
            search_obj:Search = form.save(commit=False)
            news_list:list = search_news(request,search_obj.search_request)
            context = {'news_list':news_list}
            logger.debug("Search request successfully processed!")
            return render(request, 'news/index.html', context)
    
    context = {'form': form}
    return render(request, 'news/search.html', context)

def sign_view(request):
    return user_sign(request)

def signout_view(request):
    return user_signout(request)

def register_view(request):
    return user_register(request)


def seealso_view(request):
    return render(request,'news/seealso.html')

def info_view(request):
    return render(request,'news/info.html')