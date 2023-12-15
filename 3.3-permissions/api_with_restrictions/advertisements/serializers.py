from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from advertisements.models import Advertisement


class UserSerializer(serializers.ModelSerializer):
    """Serializer для пользователя."""

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name',
                  'last_name',)


class AdvertisementSerializer(serializers.ModelSerializer):
    """Serializer для объявления."""

    class Meta:
        model = Advertisement
        fields = ('id', 'title', 'description', 'status', 'created_at',)
        read_only_fields = ['creator', ]

    def create(self, validated_data):
        """Метод для создания"""
        # Простановка значения поля создатель по-умолчанию.
        # Текущий пользователь является создателем объявления
        # изменить или переопределить его через API нельзя.
        # обратите внимание на `context` – он выставляется автоматически
        # через методы ViewSet.
        # само поле при этом объявляется как `read_only=True`
        validated_data["creator"] = self.context["request"].user
        return super().create(validated_data)

    def validate(self, data):
        """Метод для валидации. Вызывается при создании и обновлении."""
        creator = self.context["request"].user
        ads_count = Advertisement.objects.filter(creator=creator, status='OPEN').count()  # фильтруем по пользователю и статусу и считаем количество
        if ads_count >= 10 and data.status != 'CLOSED':  # проверяем, если больше 10 открытых объявлений
            raise serializers.ValidationError('Error')  # выбрасываем ошибку
        return data