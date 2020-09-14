from django.db import models
from django.urls import reverse
from .caretaker import Caretaker


class Patient(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    diagnosis = models.CharField(max_length=100)
    year_of_birth = models.IntegerField()
    caretaker = models.ForeignKey(
        Caretaker, related_name="caretakerspatients", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = ("patient")
        verbose_name_plural = ("patients")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
