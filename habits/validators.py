from rest_framework.serializers import ValidationError
class ContentValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        temp_val = dict(value).get(self.field)
        if not('www.youtube.com' in temp_val):
            raise ValidationError("Content is not valid")