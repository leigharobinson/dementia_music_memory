from django.db import models
from .caretaker import Caretaker
from .facility import Facility


class FacilityCaretaker(models.Model):
    """
    Creates the join table for the many to many relationship between caretaker and patient
    Author: Leigha
    methods: none
    """

    caretaker = models.ForeignKey(
        Caretaker, related_name="facilitiescaretakers", on_delete=models.CASCADE)
    facility = models.ForeignKey(
        Facility, related_name="facilitiescaretakers", on_delete=models.CASCADE)
