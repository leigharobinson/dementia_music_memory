from django.db import models


class EyeContact(models.Model):

    description = models.CharField(max_length=1000)

    class Meta:
        verbose_name = ("eye contact")

    def __str__(self):
        return self.description
