import random

from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db.models import Q
from datetime import datetime, timedelta
from django.utils import timezone

User = get_user_model()


def check_user_exist(new_phone):
    if User.objects.filter(phoneNumber=new_phone).exists():
        raise ValidationError([
            ValidationError('این شماره موبایل قبلا ثبت شده است!', code='phone'),
        ])


def check_reset_password_sent(user):
    reset_password = user.password_resets.last()
    if reset_password:
        today = timezone.now()
        expiration = reset_password.created_at + timedelta(minutes=1)

        if today > expiration:
            return True

        return False

    return True
