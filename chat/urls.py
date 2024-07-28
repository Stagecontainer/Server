from django.urls import path
from .views import ChatRoomCreateView, ChatMessageCreateView, ChatRoomDetailView, ChatRoomListView

urlpatterns = [
    path('room/', ChatRoomCreateView.as_view(), name='room-create'),
    path('rooms/', ChatRoomListView.as_view(), name='room-list'),
    path('room/<int:id>/', ChatRoomDetailView.as_view(), name='room-detail'),
    path('message/', ChatMessageCreateView.as_view(), name='message-create'),
]
