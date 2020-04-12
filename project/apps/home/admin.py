from django.contrib import admin
from .forms import SortingForm
from .models import Sorting


@admin.register(Sorting)
class SortingAdmin(admin.ModelAdmin):
    list_display = (
        'algorithm', 
        'numbers',
        )
    list_filter = ('algorithm',)
    form = SortingForm