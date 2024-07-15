from django import forms
from .models import Drug, CategoryDrug
# from jalali_date.fields import JalaliDateField
# from jalali_date.widgets import AdminJalaliDateWidget
# from django_jalali.forms import jDateField
# from django_jalali.admin.widgets import AdminjDateWidget,AdminSplitjDateTime


class CategoryDrugForm(forms.ModelForm):
    class Meta:
        model = CategoryDrug
        fields = "__all__"



# class DrugForm(forms.ModelForm):
#     class Meta:
#         model = Drug
#         fields = "__all__"

#     def __init__(self, *args, **kwargs):
#         super(DrugForm, self).__init__(*args, **kwargs)
#         self.fields['expiration_date'] = JalaliDateField(
#             label=("تاریخ انقضا"), widget=AdminJalaliDateWidget)


class DrugForm(forms.ModelForm):
    expiration_date = forms.DateField(widget=forms.DateInput(attrs={
        'class': 'form-control',
        'type': 'date'
    }))

    class Meta:
        model = Drug
        fields = "__all__"
