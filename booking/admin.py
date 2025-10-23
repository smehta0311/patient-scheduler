# booking/admin.py
from django.contrib import admin
from .models import Provider, Availability, Appointment


class AvailabilityInline(admin.TabularInline):
    model = Availability
    extra = 1  # show one blank row by default
    fields = ("start", "end")


@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    list_display = ("name", "user")
    search_fields = ("name", "user__username")
    inlines = [AvailabilityInline]  # add Availability rows under Provider


@admin.register(Availability)
class AvailabilityAdmin(admin.ModelAdmin):
    list_display = ("provider", "start", "end")
    list_filter = ("provider",)
    ordering = ("provider", "start")


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("patient", "provider", "starts_at", "ends_at", "status")
    list_filter = ("provider", "status")
    ordering = ("-starts_at",)
