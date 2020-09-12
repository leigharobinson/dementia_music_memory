from django.db import models
from django.urls import reverse


class Facility(models.Model):
    facility_name = models.CharField(max_length=55)
    address = models.CharField(max_length=55)

    class Meta:
        verbose_name = ("facility")
        verbose_name_plural = ("facilities")

    def get_absolute_url(self):
        return reverse("facility-detail", kwargs={"pk": self.pk})
