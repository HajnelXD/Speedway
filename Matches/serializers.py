from rest_framework import serializers

from Matches.models import Match, MatchPoints
from Teams.serializers import TeamSerializer
from Riders.seralizers import RiderSerializer


class MatchSetializer(serializers.Serializer):
    home_team = TeamSerializer(many=False)
    home_team_points = serializers.IntegerField()
    guest_team = TeamSerializer(many=False)
    guest_team_points = serializers.IntegerField()
    date = serializers.DateField()
    isFinished = serializers.BooleanField()
    queue = serializers.IntegerField()
    playoff = serializers.BooleanField()

    class Meta:
        model = Match
        fields = (
            'home_team',
            'home_team_points',
            'guest_team',
            'guest_team_points',
            'date',
            'isFinished',
            'queue',
            'playoff',
        )


class MatchPointsSerializer(serializers.Serializer):
    rider = RiderSerializer(many=False)
    match = MatchSetializer(many=False)
    first_run = serializers.IntegerField()
    second_run = serializers.IntegerField()
    third_run = serializers.IntegerField()
    fourth_run = serializers.IntegerField()
    fifth_run = serializers.IntegerField()
    sixth_run = serializers.IntegerField()
    seventh_run = serializers.IntegerField()
    joker_rider = serializers.IntegerField()
    runs = serializers.CharField()

    class Meta:
        model = MatchPoints
        fields = (
            'rider',
            'match',
            'first_run',
            'second_run',
            'third_run',
            'fourth_run',
            'fifth_run',
            'sixth_run',
            'seventh_run',
            'joker_rider',
            'runs',
        )
