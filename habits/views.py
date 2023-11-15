from flask import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
from habits.models import Habit
from habits.paginators import HabitPagination
from habits.permissions import IsOwner
from habits.serializers import HabitSerializer
from rest_framework import status


class HabitListAPIView(generics.ListAPIView):
    serializer_class = HabitSerializer
    pagination_class = HabitPagination
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Habit.objects.filter(Q(id_user=user) | Q(is_public=True))


class HabitRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated,]
    def get_queryset(self):
        user = self.request.user
        return Habit.objects.filter(id_user=user)

class HabitCreateAPIView(generics.CreateAPIView):
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_habit = serializer.save()
        new_habit.id_user = self.request.user
        new_habit.save()

class HabitUpdateAPIView(generics.UpdateAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsOwner]


class HabitDestroyAPIView(generics.DestroyAPIView):
    queryset = Habit.objects.all()
    permission_classes = [IsOwner]