from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, UpdateView, CreateView
from acl.mixins import PermissionMixin
from .filters import ReceptionFilters
from .models import Insurance
from .forms import InsuranceForm


# Create your views here.
class InsuranceListView(PermissionMixin, ListView):
    permissions = ['insurances_list']
    model = Insurance
    context_object_name = 'insurances'
    ordering = ['-created_at']
    template_name = 'insurances/list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        return ReceptionFilters(data=self.request.GET, queryset=queryset).qs


class InsuranceCreateView(PermissionMixin, CreateView):
    permissions = ['insurances_create']
    template_name = "insurances/form.html"
    model = Insurance
    form_class = InsuranceForm
    success_url = reverse_lazy("insurance-list")


class InsuranceUpdateView(PermissionMixin, UpdateView):
    permissions = ['insurances_edit']
    template_name = "insurances/form.html"
    model = Insurance
    form_class = InsuranceForm
    success_url = reverse_lazy("insurance-list")


class InsuranceDeleteView(PermissionMixin, DeleteView):
    permissions = ['insurances_delete']
    model = Insurance
    template_name = 'insurances/confirm_delete.html'
    success_url = reverse_lazy("insurance-list")

    def dispatch(self, *args, **kwargs):
        response = super().dispatch(*args, **kwargs)
        messages.success(self.request, 'آیتم مورد نظر با موفقیت حذف شد.')
        return response
