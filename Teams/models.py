from django.db import models


class Year(models.Model):
    year = models.IntegerField(unique=True)

    def __str__(self):
        return str(self.year)


class Team(models.Model):
    team_name = models.CharField(max_length=64, unique=True)
    stadium = models.CharField(max_length=256, unique=True)
    team_photo = models.CharField(max_length=32, blank=True)

    def __str__(self):
        return self.team_name


class TeamInfo(models.Model):
    team_name = models.OneToOneField(Team, on_delete=models.CASCADE)
    years_in_ekstraliga = models.ManyToManyField(Year)

    def __str__(self):
        return self.team_name.team_name
