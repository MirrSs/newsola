from django.urls import path

from . import views

urlpatterns = [
    path('<str:category>', views.index, name='index'),
    path('',views.general_view,name='general'),
    #auth
    path('user/sign',views.sign_view,name='signin'),
    path('user/signout',views.signout_view,name='signout'),
    path('user/register',views.register_view,name='register'),
    path('seealso',views.seealso_view,name='seealso'),
    path('info',views.info_view,name='info')
]