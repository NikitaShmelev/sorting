from django.contrib import admin
from django.urls import path, include
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('algorithm', views.algorithm, name='algorithm'),
    # path('algorithm/bubble', HomePageViews.bubble, name='bubble'),
    # path('algorithm/insertion', HomePageViews.insertion, name='insertion'),
    # path('algorithm/merge', HomePageViews.merge, name='merge'),
]