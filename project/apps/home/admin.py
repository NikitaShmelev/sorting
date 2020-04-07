from django.contrib import admin
from .forms import SortingForm
from .models import Sorting


@admin.register(Sorting)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = (
        'algorithm', 
        'numbers',
        )
    form = SortingForm