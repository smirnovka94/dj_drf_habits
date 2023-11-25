from rest_framework import generics
from users.models import User
from users.serializers import UserSerializer

class UserListAPIView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer

class UserUpdateAPIView(generics.UpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class UserRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()