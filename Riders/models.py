from django.db import models
from Teams.models import Year, Team


class Rider(models.Model):
    last_name = models.CharField(max_length=32)
    first_name = models.CharField(max_length=32)

    class Meta:
        unique_together = ('last_name', 'first_name')
        ordering = ['last_name']

    def __str__(self):
        return self.first_name + " " + self.last_name


class RiderInfo(models.Model):
    rider = models.ForeignKey(Rider, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    year = models.ForeignKey(Year, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('rider', 'year', 'team')
        ordering = ['team']

    def __str__(self):
        return str(self.rider) + " " + str(self.year) + " " + str(self.team)