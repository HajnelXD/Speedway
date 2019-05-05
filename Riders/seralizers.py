from django.db import IntegrityError
from rest_framework import serializers
from Riders.models import Rider


class RiederSerializer(serializers.Serializer):
    last_name = serializers.CharField()
    first_name = serializers.CharField()

    class Meta:
        model = Rider
        fields = ('last_name', 'first_name')

    def create(self, validated_data):
        try:
            return Rider.objects.create(**validated_data)
        except IntegrityError:
            raise serializers.ValidationError("Ten zawodnik już jest w bazie")
