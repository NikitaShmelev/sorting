from django import forms

from .models import Sorting


class SortingForm(forms.ModelForm):
    class Meta:
        model = Sorting
        fields = ["algorithm", "file"]

    file = forms.FileField(label="Upload File")
