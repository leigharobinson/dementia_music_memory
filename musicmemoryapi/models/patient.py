from django.db import models
from django.urls import reverse
from .facility import Facility


class Patient(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    diagnosis = models.CharField(max_length=100)
    year_of_birth = models.IntegerField()
    facility = models.ForeignKey(Facility,
                                 related_name="facility",
                                 on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("patient")
        verbose_name_plural = ("patients")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
