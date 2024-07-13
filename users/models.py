import json
import time
import requests
from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from django.utils import timezone
from django.utils.crypto import get_random_string
from django.conf.urls.static import static
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from acl.permissions import PERMISSIONS
from extenstions.utils import jalali_converter
from utils.validator import mobile_regex, mobile_validator, national_id_regex
from .helpers import MARITAL_STATUS_CHOICES
from .managers import UserManager
from django.conf import settings
from django.utils.text import slugify


# Create your models here.


def upload_image(instance, filename):
    path = 'uploads/' + 'users/' + \
           slugify(instance.email, allow_unicode=True)
    name = str(time.time()) + '-' + str(instance.username) + '-' + filename
    return path + '/' + name


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(
        max_length=100,
        verbose_name="نام",
    )
    last_name = models.CharField(
        max_length=100,
        verbose_name="نام خانوادگی"
    )
    phoneNumber = models.CharField(verbose_name="شماره موبایل", max_length=11, unique=True, validators=[mobile_regex],
                                   null=True, )
    email = models.EmailField(('ایمیل'), unique=True)
    national_id = models.CharField(
        unique=True,
        max_length=10,
        default="",
        verbose_name="کد ملی",
        validators=[national_id_regex],
    )

    father_name = models.CharField(
        null=True,
        blank=True,
        max_length=60,
        verbose_name="نام پدر",
    )

    marital_status = models.CharField(
        null=True,
        blank=True,
        max_length=128,
        verbose_name='وضعیت تاهل',
        choices=MARITAL_STATUS_CHOICES,
    )
    address = models.TextField(
        null=True,
        blank=True,
        verbose_name='آدرس'
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="تاریخ ثبت"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="تاریخ ویرایش"
    )
    is_superuser = models.BooleanField(('ادمین هست؟'), default=False)
    is_active = models.BooleanField(('active'), default=True)
    is_staff = models.BooleanField(('is staff'), default=False)
    image = models.ImageField(('تصویر'), upload_to='uploads/', null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'phoneNumber'
    REQUIRED_FIELDS = ['national_id']

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    def __str__(self):
        return self.full_name

    def jcreated(self):
        return jalali_converter(self.created_at)

    def save(self, *args, **kwargs):
        if self.phoneNumber:
            self.phoneNumber = mobile_validator(
                str(self.phoneNumber)[:11]
            )

        if self.phoneNumber:
            qs = User.objects.filter(
                phoneNumber=self.phoneNumber
            )
            if self.pk:
                qs = qs.exclude(id=self.pk)
            if qs.exists():
                raise ValidationError(
                    'شماره موبایل تکراری است و برای کاربر دیگری استفاده شده است!',
                    code="mobile"
                )

        if self.national_id:
            qs = User.objects.filter(
                national_id=self.national_id
            )
            if self.pk:
                qs = qs.exclude(id=self.pk)
            if qs.exists():
                raise ValidationError(
                    'کدملی تکراری است و برای کاربر دیگری استفاده شده است!',
                    code="national_id"
                )

        return super().save(*args, **kwargs)

    def get_phone(self):
        return self.phoneNumber

    @property
    def full_name(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        return self.national_id or '---'

    def user_role(self):
        return self.role if hasattr(self, 'role') else None

    @property
    def role_code(self):
        if hasattr(self, 'role') and self.role.role:
            return self.role.role.code
        else:
            return None

    @property
    def role_code_display(self):
        return self.role.role_name if hasattr(self, 'role') else 'کاربر'

    @property
    def has_role(self):
        if hasattr(self, 'role'):
            return True
        return False

    def change_role(self, role):
        from acl.models import UserRole
        user_role, _ = UserRole.objects.get_or_create(user=self)
        user_role.role = role
        user_role.save()
        return True

    @property
    def permissions(self):
        if self.is_superuser:
            return PERMISSIONS
        else:
            try:
                return self.user_permission.permissions_list
            except:
                return []

    def check_has_permission(self, permission):
        if permission in self.permissions:
            return True
        return False

    def get_avatar(self):
        return self.image.url if self.image else 'static/img/user-3.jpg'
