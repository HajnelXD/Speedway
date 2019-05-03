from django.db import models


class Year(models.Model):
    year = models.IntegerField(unique=True, blank=False)

    def __str__(self):
        return str(self.year)
