from rest_framework import generics
from ..models import Order, OrderItem
from medicines.models import Drug
from medicines.api.serializers import DrugSerializer
from .serializers import OrderSerializer, OrderItemSerializer
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated


class DrugListView(generics.ListAPIView):
    queryset = Drug.objects.all()
    serializer_class = DrugSerializer
    permission_classes = [IsAuthenticated]


class DrugDetailView(generics.RetrieveAPIView):
    queryset = Drug.objects.all()
    serializer_class = DrugSerializer
    lookup_field = 'pk'
    permission_classes = [IsAuthenticated]


class AddToOrderView(generics.CreateAPIView):
    serializer_class = OrderItemSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        drug_id = request.data.get('drug_id')
        quantity = int(request.data.get('quantity'))
        drug = get_object_or_404(Drug, id=drug_id)

        order, created = Order.objects.get_or_create(
            user=request.user, is_paid=False)
        order_item, created = OrderItem.objects.get_or_create(
            order=order, drug=drug, defaults={'quantity': quantity, 'price': drug.price})

        if not created:
            order_item.quantity += quantity
            order_item.save()

        return self.get_serializer(order_item).data


class OrderSummaryView(generics.RetrieveAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return Order.objects.filter(user=self.request.user, is_paid=False).first()


class PaymentView(generics.UpdateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        order = Order.objects.filter(user=request.user, is_paid=False).first()
        if order:
            order.is_paid = True
            order.save()
        return self.get_serializer(order).data
