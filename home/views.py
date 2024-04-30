from random import randint
from typing import Any

from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, View

from .algorithms import Algorithm
from .forms import SortingForm
from .models import Sorting


class HomePageView(TemplateView):
    template_name = "index.html"
    form_class = SortingForm

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["form"] = SortingForm()
        return context

    def post(self, request, *args, **kwargs):
        try:
            if request.method == "POST":
                file = request.FILES["sentFile"].open()
                list_to_sort = [
                    int(i) for i in file.readline().decode("utf-8").split(",")
                ]

                sort = SortingForm(request.POST)["algorithm"].value()
                if sort == "Bubble":
                    result = Algorithm.bubble(list_to_sort)
                elif sort == "Insertion":
                    result = Algorithm.insertion(list_to_sort)
                elif sort == "Merge":
                    result = Algorithm.merge(list_to_sort)
                elif sort == "Shell":
                    result = Algorithm.shell(list_to_sort)

                messages.success(
                    request, f"Execution time is {round(result[1], 5)} seconds"
                )

        except Exception as e:
            raise e
            messages.warning(request, f"Upload correct file in txt format")

        return HttpResponseRedirect("../../")
