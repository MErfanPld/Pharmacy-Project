# serializers.py
from rest_framework import serializers
from ..models import Ticket, Message, ChatMessage

from users.models import User
from users.api.serializers import UserSerializer


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'ticket', 'sender', 'content', 'created_at']


class TicketSerializer(serializers.ModelSerializer):
    messages = MessageSerializer(many=True, read_only=True)

    class Meta:
        model = Ticket
        fields = ['id', 'user', 'admin', 'subject', 'description',
                  'status', 'created_at', 'updated_at', 'messages']


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatMessage
        fields = ['id', 'sender', 'reciever', 'message', 'is_read', 'date']
