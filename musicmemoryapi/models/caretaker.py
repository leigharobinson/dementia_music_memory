from django.db import models
from django.db.models import F
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Caretaker(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=55)

    class Meta:
        verbose_name = ("caretaker")
        verbose_name_plural = ("caretakers")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
