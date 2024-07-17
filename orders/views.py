from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Order, OrderItem
from .forms import OrderItemForm
from medicines.models import Drug
from acl.mixins import PermissionMixin
from django.contrib import messages

# Create your views here.


def drug_list(request):
    drugs = Drug.objects.all()
    return render(request, 'orders/drug_list.html', {'drugs': drugs})


def drug_detail(request, pk):
    drug = get_object_or_404(Drug, pk=pk)
    return render(request, 'orders/drug_detail.html', {'drug': drug})


def add_to_order(request):
    if request.method == 'POST':
        drug_id = request.POST.get('drug_id')
        quantity = int(request.POST.get('quantity'))
        drug = get_object_or_404(Drug, id=drug_id)

        order, created = Order.objects.get_or_create(
            user=request.user, is_paid=False)
        order_item, created = OrderItem.objects.get_or_create(
            order=order, drug=drug, defaults={'quantity': quantity, 'price': drug.price})

        if not created:
            order_item.quantity += quantity
            order_item.save()

        return redirect('order_summary')
    return redirect('drug_list')


def order_summary(request):
    order = Order.objects.filter(user=request.user, is_paid=False).first()
    return render(request, 'orders/order_summary.html', {'order': order})


def payment(request):
    order = Order.objects.filter(user=request.user, is_paid=False).first()
    if request.method == 'POST':
        # در اینجا می‌توانید منطق پرداخت را اضافه کنید
        order.is_paid = True
        order.save()
        return redirect('drug_list')
    return render(request, 'orders/payment.html', {'order': order})


class OrderItemListView(LoginRequiredMixin, ListView):
    model = OrderItem
    template_name = 'orders/list.html'
    context_object_name = 'orders'

    def get_queryset(self):
        if self.request.user.is_superuser:
            return OrderItem.objects.all()
        else:
            return OrderItem.objects.filter(order__user=self.request.user)


class OrderAdminUpdateView(PermissionMixin, UpdateView):
    template_name = "orders/form.html"
    model = OrderItem
    form_class = OrderItemForm
    success_url = reverse_lazy("order-list")


class OrderAdminDeleteView(PermissionMixin, DeleteView):
    model = OrderItem
    template_name = 'orders/confirm_delete.html'
    success_url = reverse_lazy("order-list")

    def dispatch(self, *args, **kwargs):
        response = super().dispatch(*args, **kwargs)
        messages.success(self.request, 'آیتم مورد نظر با موفقیت حذف شد.')
        return response
