from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model

User = get_user_model()

class UserTests(APITestCase):
    def test_user_signup(self):
        url = reverse('signup')
        data = {
            'username': 'test',
            'password': '1234',
            'name': 'Test User'
        }
        response = self.client.post(url, data, format='json')
        print(f'Signup Response: {response.data}')  # 출력 추가
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, 'test')

    def test_user_login(self):
        # 먼저 회원가입을 통해 유저를 생성
        self.test_user_signup()
        
        url = reverse('token_obtain_pair')
        data = {
            'username': 'test',
            'password': '1234'
        }
        response = self.client.post(url, data, format='json')
        print(f'Login Response: {response.data}')  # 출력 추가
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)
        return response

    def test_token_refresh(self):
        # 로그인 후 토큰 발급
        login_response = self.test_user_login()
        refresh_token = login_response.data['refresh']
        
        print(f'Original Refresh Token: {refresh_token}')  # 출력 추가

        url = reverse('token_refresh')
        data = {
            'refresh': refresh_token
        }
        response = self.client.post(url, data, format='json')
        print(f'Token Refresh Response: {response.data}')  # 출력 추가
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
