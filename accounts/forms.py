from django import forms
from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator
from django.contrib import messages
from django.urls import resolve

from utils.validator import mobile_regex

User = get_user_model()


class RegisterForm(forms.ModelForm):
    password2 = forms.CharField(max_length=100, required=True, widget=forms.PasswordInput(), label='تکرار رمز عبور')

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'national_id', 'phoneNumber', 'password', 'password2']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super().__init__(*args, **kwargs)
        self.fields['password'].widget = forms.PasswordInput()

    def clean_password2(self):
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")

        if password != password2:
            raise forms.ValidationError('رمز عبور با تکرار آن مغایرت دارد!')

        return password2

    def save(self, commit=True):
        password = self.cleaned_data.pop('password', None)
        user = super().save(False)

        if password:
            user.set_password(password)
        user.save()

        self.request.session['verify_phone'] = user.phoneNumber
        messages.success(self.request, 'ثبت نام شما با موفقیت انجام شد.')
        return user
