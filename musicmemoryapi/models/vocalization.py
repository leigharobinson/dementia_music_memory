from django.db import models


class Vocalization(models.Model):

    description = models.CharField(max_length=1000)

    class Meta:
        verbose_name = ("vocaliztion")

    def __str__(self):
        return self.description
