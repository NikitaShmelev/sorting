from django.contrib import admin
from django.urls import include, path

from .views import HomePageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home_page"),
    path("algorithm", HomePageView.algorithm, name="algorithm"),
]
