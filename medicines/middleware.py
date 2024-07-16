from datetime import datetime, timedelta
from django.contrib import messages
from .models import Drug

class DrugAlertMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        if not hasattr(request, 'alerts_added') or not request.alerts_added:
            self.add_alerts(request)
            request.alerts_added = True

    def add_alerts(self, request):
        # هشدارهای موجودی کم
        low_stock_drugs = Drug.objects.filter(quantity__range=(1, 10))
        for drug in low_stock_drugs:
            message = f'تعداد {drug.name} کمتر از {drug.quantity} هست.'
            messages.warning(request, message)

        # هشدارهای موجودی صفر
        end_stock_threshold = 0
        end_stock_drugs = Drug.objects.filter(quantity__lte=end_stock_threshold)
        for drug in end_stock_drugs:
            message = f'محصول {drug.name} به اتمام رسیده هست.'
            messages.error(request, message)

        # هشدارهای تاریخ انقضا نزدیک
        today = datetime.today().date()
        expiry_threshold = today + timedelta(days=1)
        near_expiry_drugs = Drug.objects.filter(expiration_date__lte=expiry_threshold)
        for drug in near_expiry_drugs:
            message = f'تاریخ انقضای {drug.name} نزدیک است ({drug.expiration_date}).'
            messages.error(request, message)
