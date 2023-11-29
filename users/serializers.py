from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """Переопределям метод для записи хэшированного пароля в БД"""
        password = validated_data.pop("password", None)
        instance = self.Meta.model(**validated_data, is_active=True)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
