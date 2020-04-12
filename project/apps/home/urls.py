from django.contrib import admin
from django.urls import path, include
from .views import HomePageViews 

urlpatterns = [
    path('', HomePageViews.index, name='index'),
    path('algorithm', HomePageViews.algorithm, name='algorithm'),
]