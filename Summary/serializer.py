from Summary.models import SummaryTable
from rest_framework import serializers

from Teams.serializers import YearSerializer, TeamSerializer


class SummaryTableSerializer(serializers.Serializer):
    name = TeamSerializer(many=False)
    matches = serializers.IntegerField()
    points = serializers.IntegerField()
    bonus = serializers.IntegerField()
    small_points = serializers.IntegerField()
    wins = serializers.IntegerField()
    draws = serializers.IntegerField()
    losers = serializers.IntegerField()
    year = YearSerializer(many=False)

    class Meta:
        model = SummaryTable
        fields = ('name', 'matches', 'points', 'bonus', 'small_points', 'wins'
                  'draws', 'losers', 'year')
