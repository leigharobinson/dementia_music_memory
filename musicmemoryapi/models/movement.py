from django.db import models


class Movement(models.Model):

    description = models.CharField(max_length=1000)

    class Meta:
        verbose_name = ("movement")

    def __str__(self):
        return self.description
