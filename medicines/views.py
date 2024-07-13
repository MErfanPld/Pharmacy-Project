from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, UpdateView, CreateView
from acl.mixins import PermissionMixin
from .filters import DrugFilters
from .models import Drug,CategoryDrug
from .forms import CategoryDrugForm,DrugForm


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

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        return DrugFilters(data=self.request.GET, queryset=queryset).qs


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
