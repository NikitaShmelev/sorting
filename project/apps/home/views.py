from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.contrib import messages

from .forms import SortingForm
from .algorithms import Algorithm


from random import randint


def index(request):
    return render(request, 'index.html')


def algorithm(request):
    try:
        file = request.FILES['sentFile'].open()
        list_to_sort = [int(i) for i in file.readline().decode("utf-8").split(',')]

        if request.method == 'POST':
            sort = SortingForm(request.POST)['algorithm'].value()
            if sort == 'Bubble':
                result = Algorithm().bubble(list_to_sort)
            elif sort == 'Insertion':
                result = Algorithm().insertion(list_to_sort)
            else:
                result = Algorithm().merge(list_to_sort)
        messages.success(
            request, 
            f"\n\nExecution time is {round(result[1], 5)} seconds\n\n"
            )
    except:
        
        messages.warning(
            request, 
            f"\n\nUpload correct file in txt format\n\n"
            )
        
    return HttpResponseRedirect("../../")
    


    