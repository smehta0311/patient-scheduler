from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from .forms import BookingForm
from .models import Appointment


@login_required
def book(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            clash = Appointment.objects.filter(
                provider=data["provider"],
                starts_at__lt=data["ends_at"],
                ends_at__gt=data["starts_at"],
            ).exists()
            if clash:
                messages.error(request, "Sorry, that slot is already taken.")
            else:
                Appointment.objects.create(
                    patient=request.user,
                    provider=data["provider"],
                    starts_at=data["starts_at"],
                    ends_at=data["ends_at"],
                )
                messages.success(request, "Appointment booked!")
                return redirect("book")
    else:
        form = BookingForm()
    return render(request, "booking/book.html", {"form": form})


@login_required
def my_appointments(request):
    appts = Appointment.objects.filter(patient=request.user).order_by("-starts_at")
    return render(request, "booking/my_appointments.html", {"appts": appts})


@login_required
def dashboard(request):
    return render(request, "booking/dashboard.html")


@login_required
def cancel_appointment(request, pk):
    appt = get_object_or_404(Appointment, pk=pk, patient=request.user)
    appt.status = "CANCELED"
    appt.save(update_fields=["status"])
    messages.success(request, "Appointment canceled.")
    return redirect("my_appointments")


@login_required
def reschedule_appointment(request, pk):
    appt = get_object_or_404(Appointment, pk=pk, patient=request.user)

    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            clash = (
                Appointment.objects.filter(
                    provider=data["provider"],
                    starts_at__lt=data["ends_at"],
                    ends_at__gt=data["starts_at"],
                )
                .exclude(pk=appt.pk)
                .exists()
            )
            if clash:
                messages.error(request, "That new slot is already taken.")
            else:
                appt.provider = data["provider"]
                appt.starts_at = data["starts_at"]
                appt.ends_at = data["ends_at"]
                appt.status = "RESCHEDULED"
                appt.save()
                messages.success(request, "Appointment rescheduled.")
                return redirect("my_appointments")
    else:
        form = BookingForm(
            initial={
                "provider": appt.provider_id,
                "starts_at": appt.starts_at,
                "ends_at": appt.ends_at,
            }
        )

    return render(request, "booking/reschedule.html", {"form": form, "appt": appt})
