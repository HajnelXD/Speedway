from Summary.models import SummaryTable
from rest_framework import serializers

from Teams.serializers import YearSerializer


class SummaryTableSerializer(serializers.Serializer):
    name = serializers.CharField()
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
