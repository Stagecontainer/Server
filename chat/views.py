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

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

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
        }, status=status.HTTP_200_OK)

class ChatRoomListView(generics.ListAPIView):
    serializer_class = ChatRoomSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        participant_rooms = RoomParticipant.objects.filter(user=user).values_list('room', flat=True)
        return ChatRoom.objects.filter(id__in=participant_rooms)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)