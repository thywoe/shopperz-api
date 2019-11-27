from django.shortcuts import render
from django.http import JsonResponse
from .models import User
from .serializers import UserSerializer
from rest_framework.views import APIView

# Create your views here.

class AllViews(APIView):
    def get(self, request):
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return JsonResponse(serializer.data, status=200)
