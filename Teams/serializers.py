from Teams.models import Year, Team, TeamInfo
import datetime
from rest_framework import serializers
from django.db import IntegrityError


class YearSerializer(serializers.Serializer):
    year = serializers.IntegerField()

    def validate(self, value):
        if value['year'] <= 2006:
            raise serializers.ValidationError(
                "Rok nie może być wczęsniejszy niż 2007"
            )
        elif value['year'] > int(datetime.datetime.now().year):
            raise serializers.ValidationError(
                "Rok nie może być późniejszy niż niż bieżący"
            )
        return value

    class Meta:
        model = Year
        fields = ('year', )

    def create(self, validated_data):
        try:
            return Year.objects.create(**validated_data)
        except IntegrityError:
            raise serializers.ValidationError("Ten rok już jest w bazie")


class TeamSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    team_name = serializers.CharField()
    stadium = serializers.CharField()

    class Meta:
        model = Team
        fields = ('id', 'team_name', 'stadium')

    def create(self, validated_data):
        try:
            return Team.objects.create(**validated_data)
        except IntegrityError:
            raise serializers.ValidationError("Ta drużyna już jest w bazie")


class TeamInfoSerializer(serializers.Serializer):
    team_name = TeamSerializer(many=False)
    years_in_ekstraliga = YearSerializer(many=True)

    class Meta:
        model = TeamInfo
        fields = ('team_name', 'years_in_ekstraliga')

    def create(self, validated_data):
        years_data = validated_data.pop('years_in_ekstraliga')
        team_data = validated_data.pop('team_name')
        team_name, team = Team.objects.get_or_create(**team_data)
        try:
            all_data = TeamInfo.objects.create(
                team_name=team_name,
                **validated_data
            )
        except IntegrityError:
            raise serializers.ValidationError("Ten klub jest już w bazie")
        for year_data in years_data:
            year_in_ekstraliga, year = Year.objects.get_or_create(**year_data)
            all_data.years_in_ekstraliga.add(year_in_ekstraliga)
        return all_data
