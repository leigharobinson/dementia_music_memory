from django.db import models


class Talkativeness(models.Model):

    description = models.CharField(max_length=1000)

    class Meta:
        verbose_name = ("talkativeness")

    def __str__(self):
        return self.description
