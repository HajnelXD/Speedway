from rest_framework.views import APIView
from rest_framework.response import Response

from Matches.models import Match, MatchPoints
from Matches.serializers import MatchSetializer, MatchPointsSerializer


class SeasonMatchesView(APIView):
    """All matches in season"""

    def get(self, request, year, format=None):
        matches = Match.objects.filter(date__year=year)
        serializer = MatchSetializer(matches, many=True)
        return Response(serializer.data)


class MatchPointsView(APIView):
    """Match details"""

    def get(self, request, identifier, format=None):
        info = MatchPoints.objects.filter(match_id=identifier)
        serializer = MatchPointsSerializer(info, many=True)
        return Response(serializer.data)
