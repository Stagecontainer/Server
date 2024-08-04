import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import ChatRoom, ChatMessage
from django.contrib.auth import get_user_model
from channels.db import database_sync_to_async
from django.core.exceptions import ObjectDoesNotExist

User = get_user_model()

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_id = self.scope['url_route']['kwargs']['room_id']
        self.room_group_name = f'chat_{self.room_id}'
        
        try:
            await self.get_room(self.room_id)
        except ObjectDoesNotExist:
            await self.close()
            return
        
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        
        await self.accept()
    
    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
    
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        sender_nickname = text_data_json['sender']
        
        try:
            room = await self.get_room(self.room_id)
            sender = await self.get_user(sender_nickname)
            await self.save_message(sender, room, message)

            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'message': message,
                    'sender': sender_nickname  
                }
            )
        except ObjectDoesNotExist:
            await self.send(text_data=json.dumps({
                'type': 'error',
                'message': 'Room or user does not exist.'
            }))
    
    async def chat_message(self, event):
        message = event['message']
        sender = event['sender']
        
        await self.send(text_data=json.dumps({
            'type': 'chat.message',
            'message': message,
            'sender': sender
        }))
    
    @database_sync_to_async
    def get_room(self, room_id):
        return ChatRoom.objects.get(id=room_id)
    
    @database_sync_to_async
    def get_user(self, nickname):
        return User.objects.get(nickname=nickname)
    
    @database_sync_to_async
    def save_message(self, user, room, message):
        ChatMessage.objects.create(room=room, sender=user, message=message)