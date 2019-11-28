from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}
        
    # def create(self, validated_data):
    #     user = User.objects.create(
    #         firstname=validated_data['firstname'],
    #         lastname=validated_data['lastname'],
    #         email=validated_data['email'],
    #         phonenumber=validated_data['phonenumber'],
    #         isShopper=validated_data['isShopper']
    #     )
    #     user.set_password(validated_data['password'])
    #     user.save()
    #     return user