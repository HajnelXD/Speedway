from django.db import IntegrityError
from rest_framework import serializers
from Riders.models import Rider, RiderInfo
from Teams.serializers import YearSerializer, TeamSerializer
from Teams.models import Team, Year


class RiderSerializer(serializers.Serializer):
    last_name = serializers.CharField()
    first_name = serializers.CharField()
    birthday = serializers.DateField()
    nationality = serializers.CharField()

    class Meta:
        model = Rider
        fields = ('last_name', 'first_name', 'birthday', 'nationality')

    def create(self, validated_data):
        try:
            return Rider.objects.create(**validated_data)
        except IntegrityError:
            raise serializers.ValidationError("Ten zawodnik już jest w bazie")


class RiderInfoSerializer(serializers.Serializer):
    rider = RiderSerializer(many=False)
    team = TeamSerializer(many=False)
    year = YearSerializer(many=False)
    junior = serializers.ChoiceField(RiderInfo.JUNIOR_CHOICES)

    class Meta:
        model = RiderInfo
        fields = ('rider', 'team', 'year', 'junior')

    def create(self, validated_data):
        team = Team.objects.get_or_create(team_name=validated_data['team']['team_name'])
        rider = Rider.objects.get_or_create(
            last_name=validated_data['rider']['last_name'],
            first_name=validated_data['rider']['first_name'],
            birthday=validated_data['rider']['birthday'],
            nationality=validated_data['rider']['nationality']
        )
        year = Year.objects.get_or_create(year=validated_data['year']['year'])
        try:
            rider_info = RiderInfo.objects.create(rider=rider[0], team=team[0], year=year[0],
                                                  junior=validated_data['junior'])
            return rider_info
        except IntegrityError:
            raise serializers.ValidationError("Takie dane już są w bazie")
