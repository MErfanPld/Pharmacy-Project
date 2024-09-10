# serializers.py
from rest_framework import serializers
from ..models import Ticket, Message

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'ticket', 'sender', 'content', 'created_at']

class TicketSerializer(serializers.ModelSerializer):
    messages = MessageSerializer(many=True, read_only=True)
    
    class Meta:
        model = Ticket
        fields = ['id', 'user', 'admin', 'subject', 'description', 'status', 'created_at', 'updated_at', 'messages']
