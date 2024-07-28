from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth import get_user_model
from chat.models import ChatRoom, ChatMessage, RoomParticipant

User = get_user_model()

class ChatTests(APITestCase):
    def setUp(self):
        self.user_a = User.objects.create_user(nickname='user_a', password='password')
        self.user_b = User.objects.create_user(nickname='user_b', password='password')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user_a)

    def test_create_chat_room(self):
        url = reverse('room-create')
        data = {
            'name': 'Chat Room with User B',
            'invited_user_id': self.user_b.id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ChatRoom.objects.count(), 1)
        self.assertEqual(RoomParticipant.objects.count(), 2)

    def test_chat_room_list(self):
        room = ChatRoom.objects.create(name='Chat Room with User B')
        RoomParticipant.objects.create(room=room, user=self.user_a)
        RoomParticipant.objects.create(room=room, user=self.user_b)

        url = reverse('room-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'Chat Room with User B')

    def test_chat_room_detail(self):
        room = ChatRoom.objects.create(name='Chat Room with User B')
        RoomParticipant.objects.create(room=room, user=self.user_a)
        RoomParticipant.objects.create(room=room, user=self.user_b)
        ChatMessage.objects.create(room=room, sender=self.user_a, message='Hello User B')

        url = reverse('room-detail', args=[room.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Chat Room with User B')
        self.assertIn('messages', response.data)
        self.assertEqual(len(response.data['messages']), 1)
        self.assertEqual(response.data['messages'][0]['message'], 'Hello User B')

    def test_send_message(self):
        room = ChatRoom.objects.create(name='Chat Room with User B')
        RoomParticipant.objects.create(room=room, user=self.user_a)
        RoomParticipant.objects.create(room=room, user=self.user_b)

        url = reverse('message-create')
        data = {
            'room': room.id,
            'message': 'Hello, World!'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ChatMessage.objects.count(), 1)
        self.assertEqual(ChatMessage.objects.first().message, 'Hello, World!')
