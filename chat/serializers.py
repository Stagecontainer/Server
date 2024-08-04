from rest_framework import serializers
from .models import ChatRoom, ChatMessage, RoomParticipant

class ChatRoomSerializer(serializers.ModelSerializer):
    last_message = serializers.SerializerMethodField()

    class Meta:
        model = ChatRoom
        fields = ['id', 'name', 'last_message']

    def get_last_message(self, obj):
        last_message = obj.messages.order_by('-timestamp').first()
        return ChatMessageSerializer(last_message).data if last_message else None

class ChatMessageSerializer(serializers.ModelSerializer):
    sender = serializers.ReadOnlyField(source='sender.nickname')

    class Meta:
        model = ChatMessage
        fields = ['id', 'room', 'sender', 'message', 'timestamp']
        extra_kwargs = {'sender': {'read_only': True}}

    def create(self, validated_data):
        validated_data['sender'] = self.context['request'].user
        return super().create(validated_data)

class RoomParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomParticipant
        fields = '__all__'
