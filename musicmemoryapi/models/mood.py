from django.db import models


class Mood(models.Model):

    description = models.CharField(max_length=1000)

    class Meta:
        verbose_name = ("mood")

    def __str__(self):
        return self.description
