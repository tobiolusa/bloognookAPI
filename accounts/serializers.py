from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_ony': True}}
        
    def create(self, validated_data):
        new_user = CustomUser(username=validated_data['username'],
                                  email=validated_data['email'])
        new_user.set_password(validated_data['password'])
        new_user.save()
        return new_user
        