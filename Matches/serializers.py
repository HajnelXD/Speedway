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
    runs = serializers.IntegerField()
    bonuses = serializers.IntegerField()
    team = TeamSerializer(many=False)
    number = serializers.IntegerField()
    points = serializers.IntegerField()

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
            'number',
            'points',
        )


class TeamRidersPointsSerializer(serializers.Serializer):
    rider = RiderSerializer(many=False)
    points_sum = serializers.IntegerField()
    bonuses = serializers.IntegerField()
    matches = serializers.IntegerField()
    match_average = serializers.FloatField()
    runs = serializers.IntegerField()
    runs_average = serializers.FloatField()

    class Meta:
        fields = (
            'rider', 'points_sum', 'bonuses', 'matches', 'match_average',
            'runs', 'runs_average',
        )


class RiderStatsSerializer(serializers.Serializer):
    year = serializers.IntegerField(required=False)
    first_run = serializers.IntegerField()
    second_run = serializers.IntegerField()
    third_run = serializers.IntegerField()
    fourth_run = serializers.IntegerField()
    fifth_run = serializers.IntegerField()
    sixth_run = serializers.IntegerField()
    seventh_run = serializers.IntegerField()
    defects = serializers.IntegerField()
    exclusions = serializers.IntegerField()
    tape = serializers.IntegerField()
    fall = serializers.IntegerField()
    change = serializers.IntegerField()
    timeout = serializers.IntegerField()
    points_in_first_run = serializers.IntegerField()
    points_in_second_run = serializers.IntegerField()
    points_in_third_run = serializers.IntegerField()
    points_in_fourth_run = serializers.IntegerField()
    points_in_fifth_run = serializers.IntegerField()
    points_in_sixth_run = serializers.IntegerField()
    points_in_seventh_run = serializers.IntegerField()
    first_places = serializers.IntegerField()
    second_places = serializers.IntegerField()
    third_places = serializers.IntegerField()
    fourth_places = serializers.IntegerField()
    other_events = serializers.IntegerField()
    first_place_in_first_run = serializers.IntegerField()
    second_place_in_first_run = serializers.IntegerField()
    third_place_in_first_run = serializers.IntegerField()
    fourth_place_in_first_run = serializers.IntegerField()
    first_place_in_second_run = serializers.IntegerField()
    second_place_in_second_run = serializers.IntegerField()
    third_place_in_second_run = serializers.IntegerField()
    fourth_place_in_second_run = serializers.IntegerField()
    first_place_in_third_run = serializers.IntegerField()
    second_place_in_third_run = serializers.IntegerField()
    third_place_in_third_run = serializers.IntegerField()
    fourth_place_in_third_run = serializers.IntegerField()
    first_place_in_fourth_run = serializers.IntegerField()
    second_place_in_fourth_run = serializers.IntegerField()
    third_place_in_fourth_run = serializers.IntegerField()
    fourth_place_in_fourth_run = serializers.IntegerField()
    first_place_in_fifth_run = serializers.IntegerField()
    second_place_in_fifth_run = serializers.IntegerField()
    third_place_in_fifth_run = serializers.IntegerField()
    fourth_place_in_fifth_run = serializers.IntegerField()
    first_place_in_sixth_run = serializers.IntegerField()
    second_place_in_sixth_run = serializers.IntegerField()
    third_place_in_sixth_run = serializers.IntegerField()
    fourth_place_in_sixth_run = serializers.IntegerField()
    first_place_in_seventh_run = serializers.IntegerField()
    second_place_in_seventh_run = serializers.IntegerField()
    third_place_in_seventh_run = serializers.IntegerField()
    fourth_place_in_seventh_run = serializers.IntegerField()

    class Meta:
        fields = ('first_run', 'second_run', 'third_run', 'fourth_run',
                  'fifth_run', 'sixth_run', 'seventh_run', 'defects',
                  'exclusions', 'tape', 'fall', 'change', 'timeout',
                  'points_in_first_run', 'points_in_second_run',
                  'points_in_third_run', 'points_in_fourth_run',
                  'points_in_fifth_run', 'points_in_sixth_run',
                  'points_in_seventh_run', 'first_places', 'second_places',
                  'third_places', 'fourth_places', 'other_events',
                  'first_place_in_first_run', 'second_place_in_first_run',
                  'third_place_in_first_run', 'fourth_place_in_first_run',
                  'first_place_in_second_run', 'second_place_in_second_run',
                  'third_place_in_second_run', 'fourth_place_in_second_run',
                  'first_place_in_third_run', 'second_place_in_third_run',
                  'third_place_in_third_run', 'fourth_place_in_third_run',
                  'first_place_in_fourth_run', 'second_place_in_fourth_run',
                  'third_place_in_fourth_run', 'fourth_place_in_fourth_run',
                  'first_place_in_fifth_run', 'second_place_in_fifth_run',
                  'third_place_in_fifth_run', 'fourth_place_in_fifth_run',
                  'first_place_in_sixth_run', 'second_place_in_sixth_run',
                  'third_place_in_sixth_run', 'fourth_place_in_sixth_run',
                  'first_place_in_seventh_run', 'second_place_in_seventh_run',
                  'third_place_in_seventh_run', 'fourth_place_in_seventh_run',
                  'year'
                  )
