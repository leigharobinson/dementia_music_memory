from django.db import models
from .song import Song
from .caretaker_patient import CaretakerPatient


class Playlist(models.Model):

    caretaker_patient = models.ForeignKey(
        CaretakerPatient, on_delete=models.DO_NOTHING)
    song = models.ForeignKey(
        Song, null=True, on_delete=models.DO_NOTHING)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = ("playlist")
        verbose_name_plural = ("playlists")

    def __str__(self):
        return f'Order was created by {self.caretaker_patient.id} {self.song.id} at {self.created_at}.'
