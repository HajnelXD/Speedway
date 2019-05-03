from Teams.models import Year
import datetime
from rest_framework import serializers
from django.db import IntegrityError


class YearSerializer(serializers.Serializer):
    year = serializers.IntegerField()

    def validate(self, value):
        if value['year'] <= 2006:
            raise serializers.ValidationError("Rok nie może być wczęsniejszy niż 2007")
        elif value['year'] > int(datetime.datetime.now().year):
            raise serializers.ValidationError("Rok nie może być późniejszy niż niż bieżący")
        return value

    class Meta:
        model = Year
        fields = {'year', }

    def create(self, validated_data):
        try:
            return Year.objects.create(**validated_data)
        except IntegrityError:
            raise serializers.ValidationError("Ten rok już jest w bazie")
