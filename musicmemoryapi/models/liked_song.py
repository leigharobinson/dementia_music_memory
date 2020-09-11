from django.db import models


class LikedSong(models.Model):

    description = models.CharField(max_length=1000)

    class Meta:
        verbose_name = ("liked song")

    def __str__(self):
        return self.description
