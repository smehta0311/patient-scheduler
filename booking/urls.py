from django.urls import path
from .views import dashboard, book, my_appointments, cancel_appointment, reschedule_appointment

urlpatterns = [
    path("", dashboard, name="dashboard"),  # root → dashboard
    path("dashboard/", dashboard, name="dashboard"),  # /dashboard/ → dashboard
    path("book/", book, name="book"),
    path("my_appointments/", my_appointments, name="my_appointments"),
    path("cancel/<int:pk>/", cancel_appointment, name="cancel_appointment"),
    path("reschedule/<int:pk>/", reschedule_appointment, name="reschedule_appointment"),
]
