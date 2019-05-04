from django.db import models


class Year(models.Model):
    year = models.IntegerField(unique=True, blank=False)

    def __str__(self):
        return str(self.year)


class Team(models.Model):
    team_name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.team_name
