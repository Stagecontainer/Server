from rest_framework import generics, status
from rest_framework.response import Response
from .models import ChatRoom, ChatMessage, RoomParticipant
from .serializers import ChatRoomSerializer, ChatMessageSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model

User = get_user_model()

class ChatRoomCreateView(generics.CreateAPIView):
    queryset = ChatRoom.objects.all()
    serializer_class = ChatRoomSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        room = serializer.save()
        RoomParticipant.objects.create(room=room, user=self.request.user)
        invited_user_id = self.request.data.get('invited_user_id')
        if invited_user_id:
            invited_user = User.objects.get(id=invited_user_id)
            RoomParticipant.objects.create(room=room, user=invited_user)

class ChatMessageCreateView(generics.CreateAPIView):
    queryset = ChatMessage.objects.all()
    serializer_class = ChatMessageSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(sender=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class ChatRoomDetailView(generics.RetrieveAPIView):
    queryset = ChatRoom.objects.all()
    serializer_class = ChatRoomSerializer
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        room = self.get_object()
        messages = ChatMessage.objects.filter(room=room).order_by('timestamp')
        return Response({
            'id': room.id,
            'name': room.name,
            'messages': ChatMessageSerializer(messages, many=True).data
        })

class ChatRoomListView(generics.ListAPIView):
    serializer_class = ChatRoomSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        participant_rooms = RoomParticipant.objects.filter(user=user).values_list('room', flat=True)
        return ChatRoom.objects.filter(id__in=participant_rooms)

class ChatMessageListView(generics.ListAPIView):
    serializer_class = ChatMessageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        room_id = self.kwargs['room_id']
        return ChatMessage.objects.filter(room_id=room_id).order_by('timestamp')

class ChatRoomDeleteView(generics.DestroyAPIView):
    queryset = ChatRoom.objects.all()
    serializer_class = ChatRoomSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

    def perform_destroy(self, instance):
        ChatMessage.objects.filter(room=instance).delete()
        RoomParticipant.objects.filter(room=instance).delete()
        instance.delete()