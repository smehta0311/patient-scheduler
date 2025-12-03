from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from .forms import BookingForm
from .models import Appointment, Provider


# --- helpers ---------------------------------------------------------


def is_provider(user):
    """
    A 'provider' is any user that has a related Provider object.
    (booking.models.Provider has OneToOneField(User))
    """
    return Provider.objects.filter(user=user).exists()


# --- patient-facing views -------------------------------------------


@login_required
def dashboard(request):
    return render(
        request,
        "booking/dashboard.html",
        {"is_provider": is_provider(request.user)},
    )


@login_required
def book(request):
    """
    Patient books an appointment.
    Prevents overlapping appointments for the chosen provider.
    """
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
                    reason=data.get("reason", ""),  # <-- SAVE REASON HERE
                )
                messages.success(request, "Appointment booked!")
                return redirect("book")
    else:
        form = BookingForm()

    return render(request, "booking/book.html", {"form": form})


@login_required
def my_appointments(request):
    """
    Patient view of THEIR appointments.
    """
    appts = Appointment.objects.filter(patient=request.user).order_by("-starts_at")
    return render(request, "booking/my_appointments.html", {"appts": appts})


@login_required
def cancel_appointment(request, pk):
    """
    Patient cancels their own appointment.
    """
    appt = get_object_or_404(Appointment, pk=pk, patient=request.user)
    appt.status = "CANCELED"
    appt.save(update_fields=["status"])
    messages.success(request, "Appointment canceled.")
    return redirect("my_appointments")


@login_required
def reschedule_appointment(request, pk):
    """
    Patient reschedules their own appointment.
    """
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
                appt.reason = data.get("reason", appt.reason)  # <-- KEEP/UPDATE REASON
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
                "reason": appt.reason,  # <-- PREFILL REASON IN FORM
            }
        )

    return render(request, "booking/reschedule.html", {"form": form, "appt": appt})


# --- provider-facing views -----------------------------------------


@login_required
@user_passes_test(is_provider)
def provider_appointments(request):
    """
    Provider view of appointments booked WITH THEM.
    """
    provider = get_object_or_404(Provider, user=request.user)
    appts = Appointment.objects.filter(provider=provider).order_by("-starts_at")
    return render(request, "booking/provider_appointments.html", {"appts": appts})


@login_required
@user_passes_test(is_provider)
def provider_cancel_appointment(request, pk):
    """
    Provider cancels an appointment where they are the provider.
    """
    provider = get_object_or_404(Provider, user=request.user)
    appt = get_object_or_404(Appointment, pk=pk, provider=provider)
    appt.status = "CANCELED"
    appt.save(update_fields=["status"])
    messages.success(request, "Appointment canceled for this patient.")
    return redirect("provider_appointments")


@login_required
@user_passes_test(is_provider)
def provider_reschedule_appointment(request, pk):
    """
    Provider reschedules an appointment where they are the provider.
    """
    provider = get_object_or_404(Provider, user=request.user)
    appt = get_object_or_404(Appointment, pk=pk, provider=provider)

    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            # Force provider to be the logged-in provider
            data_provider = provider

            clash = (
                Appointment.objects.filter(
                    provider=data_provider,
                    starts_at__lt=data["ends_at"],
                    ends_at__gt=data["starts_at"],
                )
                .exclude(pk=appt.pk)
                .exists()
            )

            if clash:
                messages.error(request, "That new slot is already taken.")
            else:
                appt.provider = data_provider
                appt.starts_at = data["starts_at"]
                appt.ends_at = data["ends_at"]
                appt.reason = data.get("reason", appt.reason)  # <-- KEEP/UPDATE REASON
                appt.status = "RESCHEDULED"
                appt.save()
                messages.success(request, "Appointment rescheduled.")
                return redirect("provider_appointments")
    else:
        form = BookingForm(
            initial={
                "provider": provider.id,  # pre-fill but provider is enforced anyway
                "starts_at": appt.starts_at,
                "ends_at": appt.ends_at,
                "reason": appt.reason,  # <-- PREFILL REASON
            }
        )

    return render(request, "booking/reschedule.html", {"form": form, "appt": appt})
