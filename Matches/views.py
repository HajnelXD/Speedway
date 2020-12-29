from rest_framework.views import APIView
from rest_framework.response import Response

from Matches.models import Match, MatchPoints
from Matches.serializers import (
    MatchSetializer, MatchPointsSerializer, TeamRidersPointsSerializer
)


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


class TeamRidersPoints(APIView):
    """List team players in season with points"""

    def get(self, request, team_id, year, format=None):
        riders_points = MatchPoints.objects.filter(
            team_id=team_id,
            match__date__year=year,
        )
        riders = []
        exist = 0
        for rider_obj in riders_points:
            for rider in riders:
                if rider['rider'] == rider_obj.rider:
                    exist = 1
                    temp = rider_obj.sum_points(
                        rider['points_sum'],
                        rider['runs'],
                    )
                    rider['points_sum'] = temp[0]
                    rider['bonuses'] += rider_obj.bonuses
                    rider['matches'] += 1
                    rider['runs'] = temp[1]
                    try:
                        rider['match_average'] = round(
                            rider['points_sum'] / rider['matches'],
                            2
                        )
                    except ZeroDivisionError:
                        rider['match_average'] = 0
                    try:
                        rider['runs_average'] = round(
                            rider['points_sum'] /
                            rider['runs'],
                            2
                        )
                    except ZeroDivisionError:
                        rider['runs_average'] = 0
            if exist == 0:
                temp = rider_obj.sum_points(0, 0)
                riders_points_obj = {
                    'rider': rider_obj.rider,
                    'points_sum': temp[0],
                    'runs': temp[1],
                    'bonuses': rider_obj.bonuses,
                    'matches': 1,
                }
                try:
                    riders_points_obj['match_average'] = round(
                        riders_points_obj['points_sum'] /
                        riders_points_obj['matches'],
                        2
                    )
                except ZeroDivisionError:
                    riders_points_obj['match_average'] = 0
                try:
                    riders_points_obj['runs_average'] = round(
                        riders_points_obj['points_sum'] /
                        riders_points_obj['runs'],
                        2
                    )
                except ZeroDivisionError:
                    riders_points_obj['runs_average'] = 0
                riders.append(riders_points_obj)
            exist = 0
        serializer = TeamRidersPointsSerializer(riders, many=True)
        return Response(serializer.data)
