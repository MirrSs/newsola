from django.urls import path

from news.services.news_api import search_news

from . import views

urlpatterns = [
    path('<str:category>', views.index, name='index'),
    path('',views.general_view,name='general'),
    #auth
    path('user/sign',views.sign_view,name='signin'),
    path('user/signout',views.signout_view,name='signout'),
    path('user/register',views.register_view,name='register'),
    path('info/seealso',views.seealso_view,name='seealso'),
    path('info/about',views.info_view,name='info'),
    path('user/search',views.search_view,name='search')
]