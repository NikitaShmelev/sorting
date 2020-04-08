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
    if request.method == 'POST':
        array_to_sort = [randint(-10**4, 10**4) for i in range(10**4)]
        sort = SortingForm(request.POST)['algorithm'].value()
        if sort == 'Bubble':
            result = Algorithm().bubble(array_to_sort)
        elif sort == 'Insertion':
            result = Algorithm().insertion(array_to_sort)
        else:
            result = Algorithm().merge(array_to_sort)
    messages.success(
        request, 
        f"\n\nExecution time is {round(result[1], 5)} seconds\n\n"
        )
    return HttpResponseRedirect("../../")
    
    # return HttpResponseRedirect(','.join(array_to_sort))


    