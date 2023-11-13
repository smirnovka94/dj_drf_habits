from rest_framework import generics
# from rest_framework.permissions import IsAuthenticated

from habits.models import Habit
from habits.paginators import HabitPagination
from habits.serializers import HabitSerializer
# from users.permissions import IsOwner, IsModerator, IsNotModerator


class HabitListAPIView(generics.ListAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    pagination_class = HabitPagination


class HabitRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()


class HabitCreateAPIView(generics.CreateAPIView):
    serializer_class = HabitSerializer

class HabitUpdateAPIView(generics.UpdateAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()


class HabitDestroyAPIView(generics.DestroyAPIView):
    queryset = Habit.objects.all()
