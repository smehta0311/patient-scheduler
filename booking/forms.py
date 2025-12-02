from django import forms
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
