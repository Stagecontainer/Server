from django.urls import path
from .views import ChatRoomCreateView, ChatMessageCreateView, ChatRoomDetailView, ChatRoomListView, ChatMessageListView, ChatRoomDeleteView

urlpatterns = [
    path('room/', ChatRoomCreateView.as_view(), name='room-create'),
    path('rooms/', ChatRoomListView.as_view(), name='room-list'),
    path('room/<int:id>/', ChatRoomDetailView.as_view(), name='room-detail'),
    path('room/<int:id>/delete/', ChatRoomDeleteView.as_view(), name='room-delete'),  # 채팅방 삭제 엔드포인트 추가
    path('message/', ChatMessageCreateView.as_view(), name='message-create'),
    path('room/<int:room_id>/messages/', ChatMessageListView.as_view(), name='message-list'),
]
