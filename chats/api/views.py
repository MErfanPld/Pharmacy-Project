from rest_framework import viewsets
from rest_framework.exceptions import PermissionDenied
from django.db.models import Q

from acl.rest_mixin import RestPermissionMixin
from ..models import ChatMessage
from .serializers import ChatMessageSerializer

class ChatMessageViewSet(viewsets.ModelViewSet):
    permission_classes = [RestPermissionMixin]
    permissions = ['chats_list', 'chats_create', 'chats_edit', 'chats_delete']
    queryset = ChatMessage.objects.all()
    serializer_class = ChatMessageSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        if not self.request.user.is_staff:
            receiver = self.request.GET.get('receiver')
            if not receiver:
                raise PermissionDenied("Receiver not specified")

            q = Q(sender=self.request.user, receiver=receiver) | Q(sender=receiver, receiver=self.request.user)
            qs = qs.filter(q).distinct()

        return qs.order_by('created_at')
