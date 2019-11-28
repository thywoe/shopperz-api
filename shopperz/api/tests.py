from django.test import TestCase
from .models import User
from .serializers import UserSerializer
from rest_framework.test import APITestCase, APIClient
from django.urls import reverse

# Create your tests here.
class CreateUser(APITestCase):
    def setUp(self):
        self.user = {
            'firstname': 'john',
            'lastname': 'tunde',
            'email': 'john@gmail.com',
            'password': 'john',
            'phonenumber': '08085963214'
        }
    
    def test_create_user(self):
        url = reverse('register')
        response = self.client.post(url, self.user, format='json')
        self.asserEqual(response.status_code, status.HTTP_201_CREATED)