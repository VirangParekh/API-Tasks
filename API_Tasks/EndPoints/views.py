from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .serializers import UserRegistrationSerializer

class UserRegistrationView(CreateAPIView):

    serializer_class = UserRegistrationSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        status_code = status.HTTP_201_CREATED
        response = {
            'success' : 'True',
            'status code' : status_code,
            'message': 'User registered  successfully',
            'token': serializer.data[token]
            }
        
        return Response(response, status=status_code)

# Create your views here.
