from django.contrib import admin
from .models import Event, Registration


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "event_date", "venue", "capacity", "seat_count")
    list_filter = ("category", "event_date")
    search_fields = ("title", "venue", "description")
    prepopulated_fields = {"slug": ("title",)}
    date_hierarchy = "event_date"

    @admin.display(description="Registered / capacity")
    def seat_count(self, obj):
        return f"{obj.registration_count} / {obj.capacity}"


@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ("event", "user", "registered_at")
    list_filter = ("event", "registered_at")
    search_fields = ("event__title", "user__username", "user__email")
