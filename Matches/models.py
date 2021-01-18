import json

from django.db import models
from Teams.models import Team
from Riders.models import Rider

RUNS = [
    'first', 'second', 'third', 'fourth', 'fifth',
    'sixth', 'seventh'
]

PLACES = [
    'first_places', 'second_places', 'third_places', 'fourth_places'
]


class Match(models.Model):
    home_team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        related_name='home_team'
    )
    home_team_points = models.IntegerField(
        blank=True,
        null=True,
    )
    guest_team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        related_name='guest_team'
    )
    guest_team_points = models.IntegerField(
        blank=True,
        null=True,
    )
    date = models.DateField()
    isFinished = models.BooleanField()
    queue = models.IntegerField()
    playoff = models.BooleanField()

    class Meta:
        unique_together = ('home_team', 'guest_team', 'date')
        ordering = ['date']

    def __str__(self):
        return str(self.date) + " " + self.home_team.team_name + " " + \
               str(self.home_team_points) + " " + \
               str(self.guest_team_points) + " " + self.guest_team.team_name


class MatchPoints(models.Model):
    rider = models.ForeignKey(Rider, on_delete=models.CASCADE)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    first_run = models.CharField(max_length=2, null=True, blank=True)
    second_run = models.CharField(max_length=2, null=True, blank=True)
    third_run = models.CharField(max_length=2, null=True, blank=True)
    fourth_run = models.CharField(max_length=2, null=True, blank=True)
    fifth_run = models.CharField(max_length=2, null=True, blank=True)
    sixth_run = models.CharField(max_length=2, null=True, blank=True)
    seventh_run = models.CharField(max_length=2, null=True, blank=True)
    joker_rider = models.IntegerField()
    runs = models.IntegerField()
    bonuses = models.IntegerField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    number = models.IntegerField()
    points = models.IntegerField()

    def count_runs(self, runs):
        for run in RUNS:
            value = self.__getattribute__('{}_run'.format(run)).replace(
                '\'', ''
            )
            try:
                int(value)
                runs['{}_run'.format(run)] += 1
            except ValueError:
                if value == 'D':
                    runs['defects'] += 1
                elif value == 'W':
                    runs['exclusions'] += 1
                elif value == 'T':
                    runs['tape'] += 1
                elif value == 'U' or value == 'u':
                    runs['fall'] += 1
                elif value == '-':
                    runs['change'] += 1
                elif value == '-':
                    runs['timeout'] += 1
        return runs

    def count_points_in_runs(self, points):
        for i, run in enumerate(RUNS, 0):
            value = self.__getattribute__('{}_run'.format(run)).replace(
                '\'', ''
            )
            try:
                value = int(value)
                points['points_in_{}_run'.format(RUNS[i])] += value
            except ValueError:
                pass
        return points

    def count_places(self, places):
        for i, run in enumerate(RUNS, 0):
            value = self.__getattribute__('{}_run'.format(run)).replace(
                '\'', ''
            )
            try:
                value = int(value)
                if value == 3:
                    places['first_places'] += 1
                elif value == 2:
                    places['second_places'] += 1
                elif value == 1:
                    places['third_places'] += 1
                elif value == 0:
                    places['fourth_places'] += 1
            except ValueError:
                if value != ' ':
                    places['other_events'] += 1
        return places

    def count_places_in_runs(self, place_in_run):
        for i, run in enumerate(RUNS, 0):
            value = self.__getattribute__('{}_run'.format(run)).replace(
                '\'', ''
            )
            try:
                value = int(value)
                if value == 3:
                    place_in_run['first_place_in_{}_run'.format(run)] += 1
                elif value == 2:
                    place_in_run['second_place_in_{}_run'.format(run)] += 1
                elif value == 1:
                    place_in_run['third_place_in_{}_run'.format(run)] += 1
                elif value == 0:
                    place_in_run['fourth_place_in_{}_run'.format(run)] += 1
            except ValueError:
                pass
        return place_in_run

    def count_runs_in_year(self):
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
        for run in RUNS:
            value = self.__getattribute__('{}_run'.format(run)).replace(
                '\'', ''
            )
            try:
                int(value)
                runs['{}_run'.format(run)] += 1
            except ValueError:
                if value == 'D':
                    runs['defects'] += 1
                elif value == 'W':
                    runs['exclusions'] += +1
                elif value == 'T':
                    runs['tape'] += 1
                elif value == 'U' or value == 'u':
                    runs['fall'] += 1
                elif value == '-':
                    runs['change'] += 1
                elif value == 'M':
                    runs['timeout'] += 1
                if value != ' ':
                    runs['{}_run'.format(run)] += 1
        runs['year'] = self.__getattribute__('match').date.year
        return runs

    def count_points_in_years(self):
        points = {
            'points_in_first_run': 0,
            'points_in_second_run': 0,
            'points_in_third_run': 0,
            'points_in_fourth_run': 0,
            'points_in_fifth_run': 0,
            'points_in_sixth_run': 0,
            'points_in_seventh_run': 0,
        }
        for i, run in enumerate(RUNS, 0):
            value = self.__getattribute__('{}_run'.format(run)).replace(
                '\'', ''
            )
            try:
                value = int(value)
                points['points_in_{}_run'.format(RUNS[i])] = value
            except ValueError:
                pass
        points['year'] = self.__getattribute__('match').date.year
        return points

    def count_places_in_year(self):
        places = {
            'first_places': 0,
            'second_places': 0,
            'third_places': 0,
            'fourth_places': 0,
            'other_events': 0,
        }
        for i, run in enumerate(RUNS, 0):
            value = self.__getattribute__('{}_run'.format(run)).replace(
                '\'', ''
            )
            try:
                value = int(value)
                if value == 3:
                    places['first_places'] += 1
                elif value == 2:
                    places['second_places'] += 1
                elif value == 1:
                    places['third_places'] += 1
                elif value == 0:
                    places['fourth_places'] += 1
            except ValueError:
                if value != ' ':
                    places['other_events'] += 1
        places['year'] = self.__getattribute__('match').date.year
        return places

    def count_places_in_runs_in_year(self):
        place_in_run = {
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
        for i, run in enumerate(RUNS, 0):
            value = self.__getattribute__('{}_run'.format(run)).replace(
                '\'', ''
            )
            try:
                value = int(value)
                if value == 3:
                    place_in_run['first_place_in_{}_run'.format(run)] = 1
                elif value == 2:
                    place_in_run['second_place_in_{}_run'.format(run)] = 1
                elif value == 1:
                    place_in_run['third_place_in_{}_run'.format(run)] = 1
                elif value == 0:
                    place_in_run['fourth_place_in_{}_run'.format(run)] = 1
            except ValueError:
                pass
        place_in_run['year'] = self.__getattribute__('match').date.year
        return place_in_run

    class Meta:
        unique_together = ('rider', 'match')

    def __str__(self):
        return str(self.match.date) + ' ' + str(self.rider.last_name)
