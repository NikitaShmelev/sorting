from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.contrib import messages


from .forms import SortingForm
from .models import Sorting
from .algorithms import Algorithm

from random import randint



class  HomePageViews(Algorithm):


    def index(request):
        return render(request, 'index.html')


    def algorithm(request):
        try:
            if request.method == 'POST':
                
                file = request.FILES['sentFile'].open()
                list_to_sort = [int(i) for i in file.readline().decode("utf-8").split(',')]
                
                sort = SortingForm(request.POST)['algorithm'].value()
                if sort == 'Bubble':
                    result = Algorithm().bubble(list_to_sort)
                elif sort == 'Insertion':
                    result = Algorithm().insertion(list_to_sort)
                elif sort == 'Merge':
                    result = Algorithm().merge(list_to_sort)
                elif sort == 'Shell':
                    result = Algorithm().shell(list_to_sort)
                record = Sorting(
                    algorithm=getattr(Sorting, sort),
                    numbers=result[0],
                )
                record.save_base()
                print(messages.success.__name__)
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
    


    