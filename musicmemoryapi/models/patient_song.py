from django.db import models
from .song import Song
from .patient import Patient
from .eye_contact import EyeContact
from .talkativeness import Talkativeness
from .mood import Mood
from .movement import Movement
from .vocalization import Vocalization
from .liked_song import LikedSong


class PatientSong(models.Model):
    """
    Creates the join table for the many to many relationship between song and patient
    Author: Leigha
    methods: none
    LOOK FOR RELATED NAME INFO
    """
    created_at = models.DateField(auto_now_add=True)
    notes = models.CharField(max_length=1000)
    song = models.ForeignKey(Song,
                             related_name="patient_songs",
                             on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient,
                                related_name="patient_songs",
                                on_delete=models.CASCADE)
    eye_contact = models.ForeignKey(EyeContact,
                                    related_name="patient_songs",
                                    null=True,  # Makes column nullable in DB
                                    blank=True,  # Allows blank value on objects
                                    on_delete=models.CASCADE)
    talkativeness = models.ForeignKey(Talkativeness,
                                      related_name="patient_songs",
                                      null=True,  # Makes column nullable in DB
                                      blank=True,  # Allows blank value on objects
                                      on_delete=models.CASCADE)
    mood = models.ForeignKey(Mood,
                             related_name="patient_songs",
                             null=True,  # Makes column nullable in DB
                             blank=True,  # Allows blank value on objects
                             on_delete=models.CASCADE)
    movement = models.ForeignKey(Movement,
                                 related_name="patient_songs",
                                 null=True,  # Makes column nullable in DB
                                 blank=True,  # Allows blank value on objects
                                 on_delete=models.CASCADE)
    vocalization = models.ForeignKey(Vocalization,
                                     related_name="patient_songs",
                                     null=True,  # Makes column nullable in DB
                                     blank=True,  # Allows blank value on objects
                                     on_delete=models.CASCADE)
    liked_song = models.ForeignKey(LikedSong,
                                   related_name="patient_songs",
                                   null=True,  # Makes column nullable in DB
                                   blank=True,  # Allows blank value on objects
                                   on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("caretaker patient")
