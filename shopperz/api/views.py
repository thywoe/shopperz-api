from django.shortcuts import render
from django.http import JsonResponse
from .models import User
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework import status


# Create your views here.


class Register(APIView):
    '''
    Register a user
    ''' 
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(dict(message='profile is successfully created'), status=201)
        return JsonResponse(serializer.errors, status=400)
