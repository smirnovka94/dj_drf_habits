from rest_framework import serializers

from habits.models import Habit
from habits.validators import Related_or_Pleasant_HabitValidator


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'
        validators = [Related_or_Pleasant_HabitValidator()]