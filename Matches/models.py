import json

from django.db import models
from Teams.models import Team
from Riders.models import Rider


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
    first_run = models.CharField(max_length=2)
    second_run = models.CharField(max_length=2)
    third_run = models.CharField(max_length=2)
    fourth_run = models.CharField(max_length=2)
    fifth_run = models.CharField(max_length=2)
    sixth_run = models.CharField(max_length=2)
    seventh_run = models.CharField(max_length=2)
    joker_rider = models.IntegerField()
    runs = models.CharField(max_length=30)

    def set_runs_with_bonus(self, runs):
        self.runs_with_bonus = json.dumps(runs)

    def get_runs_with_bonus(self):
        return json.loads(self.runs_with_bonus)

    class Meta:
        unique_together = ('rider', 'match')

    def __str__(self):
        return str(self.match.date) + ' ' + str(self.rider.last_name)
