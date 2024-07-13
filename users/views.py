import os
from django.contrib.auth.forms import SetPasswordForm
from unidecode import unidecode
from django.http import FileResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from acl.mixins import SuperUserRequiredMixin, VerifiedUserMixin, PermissionMixin
from .filters import UserFilters
from .forms import *
from django.views.generic import ListView, DeleteView, UpdateView, CreateView
from django.views import View
from django.shortcuts import get_object_or_404
from django.conf import settings


class UsersListView(PermissionMixin, ListView):
    permissions = ['user_list']
    model = User
    context_object_name = 'users'
    ordering = ['-updated_at']
    template_name = 'users/admin/list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['types_filter_items'] = [{"name": i[1], "id": i[0]} for i in
                                          (('user', 'کاربران'), ('student', 'هنرجویان'), ('teacher', 'مدرسان'))]
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        return UserFilters(data=self.request.GET, queryset=queryset).qs


class UsersCreateView(PermissionMixin, CreateView):
    permissions = ['user_create']
    template_name = "users/admin/form.html"
    model = User
    form_class = UserForm
    success_url = reverse_lazy("users-list")


class UsersUpdateView(PermissionMixin, UpdateView):
    permissions = ['user_edit']
    template_name = "users/admin/form.html"
    model = User
    form_class = UserForm
    success_url = reverse_lazy("users-list")


class UsersDeleteView(PermissionMixin, DeleteView):
    permissions = ['user_delete']
    model = User
    template_name = 'users/admin/confirm_delete.html'
    success_url = reverse_lazy("users-list")

    def dispatch(self, *args, **kwargs):
        response = super().dispatch(*args, **kwargs)
        messages.success(self.request, 'آیتم مورد نظر با موفقیت حذف شد.')
        return response

##############################################################################

class UserChangePasswordView(PermissionMixin, View):
    permissions = ['user_change_password']
    form = SetPasswordForm
    template_name = 'users/admin/users/change_password.html'
    success_url = reverse_lazy("users-list")

    def get(self, req, pk):
        user = get_object_or_404(User, pk=pk)
        context = {"form": self.form(user), 'object': user}
        return render(req, self.template_name, context)

    def post(self, req, pk):
        user = get_object_or_404(User, pk=pk)
        form = self.form(user, req.POST)
        if form.is_valid():
            form.save()
            messages.success(req, 'رمزعبور با موفقیت تغییر داده شد.')
            return redirect(self.success_url)
        return render(req, self.template_name, context={"form": form})


##############################################################################


class ChangePasswordView(VerifiedUserMixin, View):
    form = SetPasswordForm
    template_name = 'users/admin/users/change_password.html'
    success_url = reverse_lazy("dashboard")

    def get(self, req):
        context = {"form": self.form(req.user), 'object': req.user}
        return render(req, self.template_name, context)

    def post(self, req):
        form = SetPasswordForm(req.user, req.POST)
        if form.is_valid():
            user = form.save()
            messages.success(req, 'رمزعبور با موفقیت تغییر داده شد.')
            return redirect(self.success_url)
        return render(req, self.template_name, context={"form": form})


class ChangeAvatarView(VerifiedUserMixin, UpdateView):
    template_name = "users/admin/users/form.html"
    model = User
    fields = ['avatar']
    success_url = reverse_lazy("dashboard")

    def get_object(self, queryset=None):
        return self.request.user


class ProfileView(VerifiedUserMixin, UpdateView):
    template_name = "users/admin/form.html"
    model = User
    fields = ['first_name', 'last_name', 'national_id', 'phoneNumber', 'avatar']
    success_url = reverse_lazy("profile")

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['phoneNumber'].widget.attrs['readonly'] = True
        form.fields['national_id'].widget.attrs['readonly'] = True
        return form

    def post(self, request, *args, **kwargs):
        request.POST._mutable = True
        request.POST['national_id'] = request.user.national_id
        request.POST['phoneNumber'] = request.user.phoneNumber
        messages.success(request, 'اطلاعات شما با موفقیت ویرایش شد.')
        return super().post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return self.request.user
