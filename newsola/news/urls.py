from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #auth
    path('/sign',views.sign_view,name='signin'),
    path('/signout',views.signout_view,name='signout'),
    path('/register',views.register_view,name='register'),
]