from rest_framework.serializers import ValidationError
class Related_or_Pleasant_HabitValidator:

    def __call__(self, attrs):
        related_habit = attrs.get('related_habit')
        is_pleasant_habit = attrs.get('is_pleasant_habit')

        if (related_habit and is_pleasant_habit) or (not related_habit and not is_pleasant_habit):
            raise ValidationError('Вы должны указать либо связанную привычку, либо признак приятной привычки')