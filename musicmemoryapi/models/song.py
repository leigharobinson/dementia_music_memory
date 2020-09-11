from django.db import models
from django.urls import reverse


class Song(models.Model):
    '''
    description: This class creates a song and its properties
    author: Leigha
    properties:
      position: The make will contain the rank of the song in its year(1-5).
      artist: This property contains the name of the artist/artist who recorded the song
      song_title: This property contains a string of the song title
      year: This property contains the year as a number

    '''
    position = models.CharField(null=True, max_length=100)
    artist = models.CharField(max_length=100)
    song_title = models.CharField(max_length=100)
    year = models.IntegerField()

    class Meta:
        verbose_name = ("song")
        verbose_name_plural = ("songs")

    def get_absolute_url(self):
        return reverse("song_detail", kwargs={"pk": self.pk})
