from django.shortcuts import render
from django.http import HttpResponseRedirect

def index(request):
    return render(request, 'index.html')


def bubble(request):
    pass


def insertion(request):
    pass


def merge(request):
    pass