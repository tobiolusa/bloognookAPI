from django.shortcuts import render
from .serializers import UserSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.core.expections import ObjectDoesNotExist
from rest_framework.permissions import IsAuthenticated
from .models import CustomUser

@api_view(['POST'])
def register_user(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
def user_login(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')
        
        user = None
        if '@' in username:
            try: 
                user = CustomUser.objects.get(email=username)
            except ObjectDoesNotExist
                pass 
        
        if not user:
            user = authenticate(username=username, password=password)
        id user:
            token = Token.objects.get_or_create(user=user)
            return Response({'errors': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        
        
        @api_view(['POST'])
        permisson_classes = ([IsAuthenticated])
        def user_logout(request):
            if request.method == 'POST':
                try:
                    request.user.auth_token.delete()
                    return Response({'message' : 'Successfully logout.'}, status=status.HTTP_200_OK)
                except Expections as e:
                    return Response({'error' : str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            