from django.contrib import admin
from django.urls import path
from . import views

urlpatterns=[
    path('register',views.register,name='register'),
    path('loginuser',views.loginuser,name='loginuser'),
    path('logout',views.logout_user,name='logout'),
]



