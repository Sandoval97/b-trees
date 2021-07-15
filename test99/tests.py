from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status


class JWTTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="test", password="test")

    def test_signin(self):
        data = {
                'username': 'test',
                'password': 'test'
                }

        response = self.client.post(reverse('signin'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotEqual(response.data, None)

    def test_refresh(self):
        payload1 = {
                    'username': 'test',
                    'password': 'test'
                    }

        response = self.client.post(reverse('signin'), payload1, format='json')

        payload2 = {
                'refresh': response.data['refresh'],
                }

        response = self.client.post(
                        reverse('refresh'),
                        payload2,
                        format='json'
                    )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotEqual(response.data, None)

    def test_verify(self):
        payload1 = {
                'username': 'test',
                'password': 'test'
                }

        response = self.client.post(reverse('signin'), payload1, format='json')

        payload2 = {
                'token': response.data['access'],
                }

        response = self.client.post(reverse('verify'), payload2, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {})
