from django.urls import path
from .views import (
    dashboard,
    book,
    my_appointments,
    cancel_appointment,
    reschedule_appointment,
    provider_appointments,
    provider_cancel_appointment,
    provider_reschedule_appointment,
)

urlpatterns = [
    # NEW: root URL -> dashboard
    path("", dashboard, name="home"),
    # Dashboard (still works at /dashboard/)
    path("dashboard/", dashboard, name="dashboard"),
    # Patient-facing
    path("book/", book, name="book"),
    path("my_appointments/", my_appointments, name="my_appointments"),
    path("cancel/<int:pk>/", cancel_appointment, name="cancel_appointment"),
    path("reschedule/<int:pk>/", reschedule_appointment, name="reschedule_appointment"),
    # Provider-facing
    path("provider/appointments/", provider_appointments, name="provider_appointments"),
    path(
        "provider/appointments/<int:pk>/cancel/",
        provider_cancel_appointment,
        name="provider_cancel_appointment",
    ),
    path(
        "provider/appointments/<int:pk>/reschedule/",
        provider_reschedule_appointment,
        name="provider_reschedule_appointment",
    ),
]
