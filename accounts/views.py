from django.contrib.auth import logout
from django.contrib.auth.forms import SetPasswordForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.views import LoginView as LoginViewAuto
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, FormView
from acl.mixins import AnonymousUserMixin
from .forms import *
from unidecode import unidecode
from django.conf import settings


class RegisterView(AnonymousUserMixin, CreateView):
    template_name = "auth/register.html"
    model = User
    form_class = RegisterForm
    success_url = reverse_lazy("users-list")

    def post(self, request, *args, **kwargs):
        request.POST._mutable = True
        request.POST['phoneNumber'] = unidecode(request.POST.get('phoneNumber'))
        request.POST['national_id'] = unidecode(request.POST.get('national_id'))
        return super().post(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'request': self.request})
        return kwargs


class LoginView(LoginViewAuto):
    template_name = 'auth/login.html'
    redirect_authenticated_user = True
    next_page = reverse_lazy('dashboard')
    success_url = reverse_lazy('dashboard')

    def post(self, request, *args, **kwargs):
        request.POST._mutable = True
        username = request.POST.get('username')
        if username:
            request.POST['username'] = unidecode(username)
        else:
            # Handle the case where username is None
            # You can set a default value or raise a validation error
            request.POST['username'] = ''
        return super().post(request, *args, **kwargs)

# TODO ERROR
class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(settings.LOGIN_URL)

    def post(self, request):
        logout(request)
        return HttpResponseRedirect(settings.LOGIN_URL)