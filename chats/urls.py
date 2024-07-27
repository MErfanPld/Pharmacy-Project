from django.urls import path
from .views import *

urlpatterns = []

dashboard_urls = [
    path('', ChatMessageListView.as_view(), name='chats-list'),
    path('<int:pk>/', ChatMessageRoomView.as_view(), name='chats-room'),
    path('delete/<int:pk>/', ChatMessagesDeleteView.as_view(), name='chats-delete'),
]

urlpatterns += dashboard_urls