from rest_framework.views import APIView
from rest_framework.response import Response
from operator import itemgetter

from Matches.models import Match, MatchPoints
from Matches.serializers import (
    MatchSetializer, MatchPointsSerializer, TeamRidersPointsSerializer,
    RiderStatsSerializer
)
from Riders.models import RiderInfo


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
                    rider['points_sum'] += rider_obj.points
                    rider['bonuses'] += rider_obj.bonuses
                    rider['matches'] += 1
                    rider['runs'] += rider_obj.runs
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
                riders_points_obj = {
                    'rider': rider_obj.rider,
                    'points_sum': rider_obj.points,
                    'runs': rider_obj.runs,
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
        riders = sorted(riders, key=itemgetter('runs_average'))
        riders.reverse()
        serializer = TeamRidersPointsSerializer(riders, many=True)
        return Response(serializer.data)


class RiderStatsVs(APIView):
    """Riders stats on stadium"""

    def get(self, request, home_team_id, team_id, year, format=None):
        riders_in_team = RiderInfo.objects.filter(
            team_id=team_id,
            year__year=year,
        )
        riders_stats = []
        for rider in riders_in_team:
            riders_stats.append({
                'id': rider.rider_id,
                'rider': rider.rider,
                'matches': 0,
                'points_sum': 0,
                'bonuses': 0,
                'match_average': 0,
                'runs': 0,
                'runs_average': 0,
            })
        finally_stats = []
        for rider_stats in riders_stats:
            stats = MatchPoints.objects.filter(
                match__home_team_id=home_team_id,
                rider_id=rider_stats['id'],
            )
            for statistic in stats:
                rider_stats['matches'] += 1
                rider_stats['points_sum'] = statistic.points
                rider_stats['bonuses'] += statistic.bonuses
                try:
                    rider_stats['match_average'] = round(
                        rider_stats['points_sum'] /
                        rider_stats['matches'],
                        2
                    )
                except ZeroDivisionError:
                    rider_stats['match_average'] = 0
                rider_stats['runs'] = statistic.runs
                try:
                    rider_stats['runs_average'] = round(
                        rider_stats['points_sum'] /
                        rider_stats['runs'],
                        2
                    )
                except ZeroDivisionError:
                    rider_stats['runs_average'] = 0
            finally_stats.append(rider_stats)
        riders = sorted(finally_stats, key=itemgetter('runs_average'))
        riders.reverse()
        serializer = TeamRidersPointsSerializer(riders, many=True)
        return Response(serializer.data)


class RiderMatchPoints(APIView):
    """List of rider match points"""

    def get(self, request, rider_id, format=None):
        matches = MatchPoints.objects.filter(
            rider_id=rider_id
        )
        serializer = MatchPointsSerializer(matches, many=True)
        return Response(serializer.data)


class RiderStats(APIView):
    """Rider stats details"""

    def get(self, request, rider_id, format=None):
        matches = MatchPoints.objects.filter(
            rider_id=rider_id
        )
        runs = {
            'first_run': 0,
            'second_run': 0,
            'third_run': 0,
            'fourth_run': 0,
            'fifth_run': 0,
            'sixth_run': 0,
            'seventh_run': 0,
            'defects': 0,
            'exclusions': 0,
            'tape': 0,
            'fall': 0,
            'change': 0,
            'timeout': 0,
        }

        points_in_run = {
            'points_in_first_run': 0,
            'points_in_second_run': 0,
            'points_in_third_run': 0,
            'points_in_fourth_run': 0,
            'points_in_fifth_run': 0,
            'points_in_sixth_run': 0,
            'points_in_seventh_run': 0,
        }
        places = {
            'first_places': 0,
            'second_places': 0,
            'third_places': 0,
            'fourth_places': 0,
            'other_events': 0,
        }
        places_in_run = {
            'first_place_in_first_run': 0,
            'second_place_in_first_run': 0,
            'third_place_in_first_run': 0,
            'fourth_place_in_first_run': 0,
            'first_place_in_second_run': 0,
            'second_place_in_second_run': 0,
            'third_place_in_second_run': 0,
            'fourth_place_in_second_run': 0,
            'first_place_in_third_run': 0,
            'second_place_in_third_run': 0,
            'third_place_in_third_run': 0,
            'fourth_place_in_third_run': 0,
            'first_place_in_fourth_run': 0,
            'second_place_in_fourth_run': 0,
            'third_place_in_fourth_run': 0,
            'fourth_place_in_fourth_run': 0,
            'first_place_in_fifth_run': 0,
            'second_place_in_fifth_run': 0,
            'third_place_in_fifth_run': 0,
            'fourth_place_in_fifth_run': 0,
            'first_place_in_sixth_run': 0,
            'second_place_in_sixth_run': 0,
            'third_place_in_sixth_run': 0,
            'fourth_place_in_sixth_run': 0,
            'first_place_in_seventh_run': 0,
            'second_place_in_seventh_run': 0,
            'third_place_in_seventh_run': 0,
            'fourth_place_in_seventh_run': 0,
        }

        for match in matches:
            runs = match.count_runs(runs)
            points_in_run = match.count_points_in_runs(points_in_run)
            places = match.count_places(places)
            places_in_run = match.count_places_in_runs(places_in_run)

        data = runs
        data.update(points_in_run)
        data.update(places)
        data.update(places_in_run)
        serializer = RiderStatsSerializer(data, many=False)
        return Response(serializer.data)


class RiderStatsInYear(APIView):
    """Rider stats details in year"""

    def get(self, request, rider_id, year, format=None):
        matches = MatchPoints.objects.filter(
            rider_id=rider_id,
            match__date__year=year,
        )

        runs = {
            'first_run': 0,
            'second_run': 0,
            'third_run': 0,
            'fourth_run': 0,
            'fifth_run': 0,
            'sixth_run': 0,
            'seventh_run': 0,
            'defects': 0,
            'exclusions': 0,
            'tape': 0,
            'fall': 0,
            'change': 0,
            'timeout': 0,
        }

        points_in_run = {
            'points_in_first_run': 0,
            'points_in_second_run': 0,
            'points_in_third_run': 0,
            'points_in_fourth_run': 0,
            'points_in_fifth_run': 0,
            'points_in_sixth_run': 0,
            'points_in_seventh_run': 0,
        }
        places = {
            'first_places': 0,
            'second_places': 0,
            'third_places': 0,
            'fourth_places': 0,
            'other_events': 0,
        }
        places_in_run = {
            'first_place_in_first_run': 0,
            'second_place_in_first_run': 0,
            'third_place_in_first_run': 0,
            'fourth_place_in_first_run': 0,
            'first_place_in_second_run': 0,
            'second_place_in_second_run': 0,
            'third_place_in_second_run': 0,
            'fourth_place_in_second_run': 0,
            'first_place_in_third_run': 0,
            'second_place_in_third_run': 0,
            'third_place_in_third_run': 0,
            'fourth_place_in_third_run': 0,
            'first_place_in_fourth_run': 0,
            'second_place_in_fourth_run': 0,
            'third_place_in_fourth_run': 0,
            'fourth_place_in_fourth_run': 0,
            'first_place_in_fifth_run': 0,
            'second_place_in_fifth_run': 0,
            'third_place_in_fifth_run': 0,
            'fourth_place_in_fifth_run': 0,
            'first_place_in_sixth_run': 0,
            'second_place_in_sixth_run': 0,
            'third_place_in_sixth_run': 0,
            'fourth_place_in_sixth_run': 0,
            'first_place_in_seventh_run': 0,
            'second_place_in_seventh_run': 0,
            'third_place_in_seventh_run': 0,
            'fourth_place_in_seventh_run': 0,
        }

        for match in matches:
            runs = match.count_runs(runs)
            points_in_run = match.count_points_in_runs(points_in_run)
            places = match.count_places(places)
            places_in_run = match.count_places_in_runs(places_in_run)

        data = runs
        data.update(points_in_run)
        data.update(places)
        data.update(places_in_run)
        serializer = RiderStatsSerializer(data, many=False)
        return Response(serializer.data)
