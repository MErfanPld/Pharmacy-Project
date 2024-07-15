from datetime import datetime, timedelta
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, UpdateView, CreateView
from acl.mixins import PermissionMixin
from .filters import DrugFilters
from .models import Drug, CategoryDrug
from .forms import CategoryDrugForm, DrugForm


# Create your views here.

# ==================== CATEGORY DRUG ====================

class CategoryDrugListView(PermissionMixin, ListView):
    permissions = ['medicines_list']
    model = CategoryDrug
    context_object_name = 'category_drugs'
    ordering = ['-created_at']
    template_name = 'medicines/category/list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        return DrugFilters(data=self.request.GET, queryset=queryset).qs


class CategoryDrugCreateView(PermissionMixin, CreateView):
    permissions = ['medicines_create']
    template_name = "medicines/category/form.html"
    model = CategoryDrug
    form_class = CategoryDrugForm
    success_url = reverse_lazy("category-drug-list")


class CategoryDrugUpdateView(PermissionMixin, UpdateView):
    permissions = ['medicines_edit']
    template_name = "medicines/category/form.html"
    model = CategoryDrug
    form_class = CategoryDrugForm
    success_url = reverse_lazy("category-drug-list")


class CategoryDrugDeleteView(PermissionMixin, DeleteView):
    permissions = ['medicines_delete']
    model = CategoryDrug
    template_name = 'medicines/category/confirm_delete.html'
    success_url = reverse_lazy("category-drug-list")

    def dispatch(self, *args, **kwargs):
        response = super().dispatch(*args, **kwargs)
        messages.success(self.request, 'آیتم مورد نظر با موفقیت حذف شد.')
        return response


# ==================== DRUG ====================


class DrugListView(PermissionMixin, ListView):
    permissions = ['medicines_list']
    model = Drug
    context_object_name = 'drugs'
    ordering = ['-created_at']
    template_name = 'medicines/list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return DrugFilters(data=self.request.GET, queryset=queryset).qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # هشدارهای موجودی کم
        low_stock_drugs = Drug.objects.filter(quantity__range=(1, 10))
        for drug in low_stock_drugs:
            message = f'تعداد {drug.name} کمتر از {drug.quantity} هست.'
            messages.warning(self.request, message)

        # هشدارهای موجودی صفر
        end_stock_threshold = 0
        end_stock_drugs = Drug.objects.filter(quantity__lte=end_stock_threshold)
        for drug in end_stock_drugs:
            message = f'محصول {drug.name} به اتمام رسیده هست.'
            messages.error(self.request, message)

        # هشدارهای تاریخ انقضا نزدیک
        today = datetime.today().date()
        expiry_threshold = today + timedelta(days=1)
        near_expiry_drugs = Drug.objects.filter(expiration_date__lte=expiry_threshold)
        for drug in near_expiry_drugs:
            message = f'تاریخ انقضای {drug.name} نزدیک است ({drug.jexpiration_date()}).'
            messages.error(self.request, message)

        return context

class DrugCreateView(PermissionMixin, CreateView):
    permissions = ['medicines_create']
    template_name = "medicines/form.html"
    model = Drug
    form_class = DrugForm
    success_url = reverse_lazy("drug-list")


class DrugUpdateView(PermissionMixin, UpdateView):
    permissions = ['medicines_edit']
    template_name = "medicines/form.html"
    model = Drug
    form_class = DrugForm
    success_url = reverse_lazy("drug-list")


class DrugDeleteView(PermissionMixin, DeleteView):
    permissions = ['medicines_delete']
    model = Drug
    template_name = 'medicines/confirm_delete.html'
    success_url = reverse_lazy("drug-list")

    def dispatch(self, *args, **kwargs):
        response = super().dispatch(*args, **kwargs)
        messages.success(self.request, 'آیتم مورد نظر با موفقیت حذف شد.')
        return response
