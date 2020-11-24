from django.db import models
from Teams.models import Team, Year


class SummaryTable(models.Model):
    name = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        related_name='team'
    )
    matches = models.SmallIntegerField()
    points = models.SmallIntegerField()
    bonus = models.SmallIntegerField()
    small_points = models.SmallIntegerField()
    wins = models.SmallIntegerField()
    draws = models.SmallIntegerField()
    losers = models.SmallIntegerField()
    year = models.ForeignKey(
        Year,
        on_delete=models.CASCADE,
        related_name='summary_year'
    )

    class Meta:
        unique_together = ('name', 'year')
        ordering = ['points']

    def __str__(self):
        return '{} {} {}'.format(self.name, self.points, self.year)
