from django.db import models
from .song import Song
from .patient import Patient
from .eye_contact import EyeContact
from .talkativeness import Talkativeness
from .mood import Mood
from .movement import Movement
from .vocalization import Vocalization
from .liked_song import LikedSong
from .caretaker import Caretaker


class SongResponse(models.Model):
    """
    Creates the join table for the many to many relationship between song and patient
    Author: Leigha
    methods: none
    LOOK FOR RELATED NAME INFO
    """
    created_at = models.DateField(auto_now_add=True)
    notes = models.CharField(max_length=1000)
    caretaker = models.ForeignKey(
        Caretaker, related_name="caretakers", null=True,
        blank=True, on_delete=models.DO_NOTHING)
    song = models.ForeignKey(
        Song, related_name="patientssongs", on_delete=models.DO_NOTHING)
    patient = models.ForeignKey(Patient,
                                related_name="patientssongs",
                                on_delete=models.DO_NOTHING)
    eye_contact = models.ForeignKey(EyeContact,
                                    related_name="patientssongs",
                                    null=True,  # Makes column nullable in DB
                                    blank=True,  # Allows blank value on objects
                                    on_delete=models.DO_NOTHING)
    talkativeness = models.ForeignKey(Talkativeness, related_name="patientssongs", null=True,  # Makes column nullable in DB
                                      blank=True,  # Allows blank value on objects
                                      on_delete=models.DO_NOTHING)
    mood = models.ForeignKey(Mood,
                             related_name="patientssongs",
                             null=True,  # Makes column nullable in DB
                             blank=True,  # Allows blank value on objects
                             on_delete=models.DO_NOTHING)
    movement = models.ForeignKey(Movement,
                                 related_name="patientssongs",
                                 null=True,  # Makes column nullable in DB
                                 blank=True,  # Allows blank value on objects
                                 on_delete=models.DO_NOTHING)
    vocalization = models.ForeignKey(Vocalization,
                                     related_name="patientssongs",
                                     null=True,  # Makes column nullable in DB
                                     blank=True,  # Allows blank value on objects
                                     on_delete=models.DO_NOTHING)
    liked_song = models.ForeignKey(LikedSong,
                                   related_name="patientssongs",
                                   null=True,  # Makes column nullable in DB
                                   blank=True,  # Allows blank value on objects
                                   on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = ("caretaker patient")
