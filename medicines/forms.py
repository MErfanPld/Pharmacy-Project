from django import forms
from .models import Drug, CategoryDrug


class CategoryDrugForm(forms.ModelForm):
    class Meta:
        model = CategoryDrug
        fields = "__all__"


class DrugForm(forms.ModelForm):
    class Meta:
        model = Drug
        fields = "__all__"


