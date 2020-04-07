from django.contrib import admin
from django.urls import path, include
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('bubble', views.bubble, name='bubble'),
    path('insertion', views.insertion, name='insertion'),
    path('merge', views.merge, name='merge'),
]