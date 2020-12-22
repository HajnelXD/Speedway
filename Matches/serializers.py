from rest_framework import serializers

from Matches.models import Match, MatchPoints
from Teams.serializers import TeamSerializer
from Riders.seralizers import RiderSerializer


class MatchSetializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
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
            'id'
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
    first_run = serializers.CharField()
    second_run = serializers.CharField()
    third_run = serializers.CharField()
    fourth_run = serializers.CharField()
    fifth_run = serializers.CharField()
    sixth_run = serializers.CharField()
    seventh_run = serializers.CharField()
    joker_rider = serializers.IntegerField()
    runs = serializers.CharField()
    bonuses = serializers.IntegerField()
    team = TeamSerializer(many=False)
    number = serializers.IntegerField()

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
            'bonuses',
            'team',
            'number'
        )
