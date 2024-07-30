from django.contrib.auth import get_user_model
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DeleteView, UpdateView, CreateView, DetailView, FormView
from django.urls import reverse_lazy
from acl.mixins import SuperUserRequiredMixin, PermissionMixin
from .filters import ChatMessageFilters
from .models import ChatMessage
from django.conf import settings
from django.contrib import messages

User = get_user_model()


class ChatMessageListView(PermissionMixin, ListView):
    permissions = ['chats_list']
    model = ChatMessage
    context_object_name = 'objects'
    ordering = ['created_at']
    template_name = 'chats/admin/list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        if not self.request.user.is_staff:
            q = Q(sender=self.request.user) | Q(receiver=self.request.user)
            queryset = queryset.filter(q).distinct()

        return ChatMessageFilters(data=self.request.GET, queryset=queryset).qs.order_by('-created_at')


class ChatMessageRoomView(PermissionMixin, DetailView):
    permissions = ['chats_create']
    template_name = "chats/admin/form.html"

    def get_queryset(self):
        if self.request.user.is_staff:
            users = User.objects.all()
        else:
            users = User.objects.filter(role__isnull=False)
        return users



class ChatMessagesDeleteView(PermissionMixin, DeleteView):
    permissions = ['chats_delete']
    model = ChatMessage
    template_name = 'chats/admin/form.html'
    success_url = reverse_lazy("chats-list")

    def get_queryset(self):
        qs = super().get_queryset()
        if not self.request.user.is_staff:
            q = Q(sender=self.request.user) | Q(receiver=self.request.user)
            qs = qs.filter(q).distinct()

        return qs.order_by('created_at')

    def dispatch(self, *args, **kwargs):
        resp = super().dispatch(*args, **kwargs)
        messages.success(self.request, 'آیتم مورد نظر با موفقیت حدف شد.')
        return resp