from datetime import timedelta

from django import forms
from django.utils import timezone

from .models import Appointment


class BookingForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ["provider", "starts_at", "ends_at", "reason"]
        widgets = {
            "starts_at": forms.TextInput(
                attrs={"class": "datetime-input", "placeholder": "Select start date & time"}
            ),
            "ends_at": forms.TextInput(
                attrs={"class": "datetime-input", "placeholder": "Select end date & time"}
            ),
            "reason": forms.Textarea(
                attrs={
                    "rows": 3,
                    "placeholder": "Briefly describe the reason for this appointment",
                }
            ),
        }

    def clean(self):
        """
        Extra validation for booking:
        - cannot book in the past
        - end time must be after start time
        - appointment must be at least 15 minutes long
        """
        cleaned_data = super().clean()
        starts_at = cleaned_data.get("starts_at")
        ends_at = cleaned_data.get("ends_at")

        # Only validate if both fields are present
        if not starts_at or not ends_at:
            return cleaned_data

        now = timezone.now()

        # 1) No booking in the past
        if starts_at < now:
            self.add_error(
                "starts_at",
                "You cannot book an appointment in the past.",
            )

        # 2) End must be after start
        if ends_at <= starts_at:
            self.add_error(
                "ends_at",
                "The end time must be later than the start time.",
            )

        # 3) Minimum duration: 15 minutes
        if ends_at - starts_at < timedelta(minutes=15):
            self.add_error(
                "ends_at",
                "Appointments must be at least 15 minutes long.",
            )

        return cleaned_data
