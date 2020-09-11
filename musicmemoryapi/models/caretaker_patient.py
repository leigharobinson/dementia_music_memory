from django.db import models
from .caretaker import Caretaker
from .patient import Patient


class CaretakerPatient(models.Model):
    """
    Creates the join table for the many to many relationship between caretaker and patient
    Author: Leigha
    methods: none
    """

    caretaker = models.ForeignKey(Caretaker,
                                  related_name="caretakers",
                                  on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient,
                                related_name="patients",
                                on_delete=models.CASCADE)
