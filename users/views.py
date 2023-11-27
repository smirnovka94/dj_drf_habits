from rest_framework import generics
from rest_framework_simplejwt.views import TokenObtainPairView

from users.models import User
from users.serializers import UserSerializer, UserRegisterSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserListAPIView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer


class UserUpdateAPIView(generics.UpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class UserRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

