from django.db import models


class Rider(models.Model):
    last_name = models.CharField(max_length=32)
    first_name = models.CharField(max_length=32)

    class Meta:
        unique_together = ('last_name', 'first_name')
        ordering = ['last_name']

    def __str__(self):
        return self.first_name + " " + self.last_name


