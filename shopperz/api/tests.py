from django.test import TestCase
from .models import User
from rest_framework import status
from .serializers import UserSerializer
from rest_framework.test import APITestCase, APIClient
from django.urls import reverse

# Create your tests here.


class CreateUser(APITestCase):
    '''
       This is use to test for register user route
       
    '''
    
    
    def setUp(self):
        self.user = {
            'firstname': 'john',
            'lastname': 'tunde',
            'email': 'john@gmail.com',
            'password': 'john',
            'phonenumber': '08085963214'
        }
        
        # self.same_email = {
        #     'firstname': 'fola',
        #     'lastname': 'shade',
        #     'email': 'john@gmail.com',
        #     'password': 'john',
        #     'phonenumber': '08085963214'
        # }
        
        self.missing_email = {
            'firstname': 'john',
            'lastname': 'tunde',
            'email': '',
            'password': 'john',
            'phonenumber': '08085963214'
        }
        
        self.empty_details = {
            'firstname': '',
            'lastname': '',
            'email': '',
            'password': '',
            'phonenumber': ''
        }
    
    def test_create_user(self):
        url = reverse('register')
        response = self.client.post(url, self.user, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
    def test_missing_email(self):
        url = reverse('register')
        response = self.client.post(url, self.missing_email, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_empty_info(self):
        url = reverse('register')
        response = self.client.post(url, self.empty_details, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    # def test_same_email(self):
    #     url = reverse('register')
    #     response = self.client.post(url, self.same_email, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)