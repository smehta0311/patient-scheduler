from django.db import models
from django.contrib.auth.models import User


class Provider(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Availability(models.Model):
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    start = models.DateTimeField()
    end = models.DateTimeField()

    def __str__(self):
        return f"{self.provider} {self.start:%Y-%m-%d %H:%M}"


class Appointment(models.Model):
    STATUS = (("BOOKED", "BOOKED"), ("CANCELED", "CANCELED"), ("RESCHEDULED", "RESCHEDULED"))
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name="patient_appointments")
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    starts_at = models.DateTimeField()
    ends_at = models.DateTimeField()
    status = models.CharField(max_length=12, choices=STATUS, default="BOOKED")

    def __str__(self):
        return f"{self.patient.username} with {self.provider} @ {self.starts_at:%m/%d %H:%M}"
