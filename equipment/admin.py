from django.contrib import admin
from django.utils import timezone
from django.utils.html import format_html

from .models import Equipment


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "serial_number",
        "location",
        "next_due_date",
        "status",
        "critical",
        "overdue_badge",
    ]
    list_filter = ["status", "condition", "critical"]
    search_fields = ["name", "serial_number", "location"]
    ordering = ["next_due_date"]

    fieldsets = (
        ("Identity", {
            "fields": ("name", "serial_number"),
        }),
        ("Location & State", {
            "fields": ("location", "status", "condition", "critical"),
        }),
        ("Service Schedule", {
            "fields": ("last_service_date", "next_due_date"),
        }),
        ("Notes", {
            "fields": ("notes",),
            "classes": ("collapse",),
        }),
        ("Audit", {
            "fields": ("created_at", "updated_at"),
            "classes": ("collapse",),
        }),
    )
    readonly_fields = ("created_at", "updated_at")

    @admin.display(description="Overdue?", ordering="next_due_date")
    def overdue_badge(self, obj):
        if obj.next_due_date is None:
            return "—"

        today = timezone.now().date()
        days = (obj.next_due_date - today).days

        if days < 0:
            return format_html(
                '<span style="color:#b91c1c;font-weight:600;">⚠ {} days overdue</span>',
                abs(days),
            )
        if days <= 14:
            return format_html(
                '<span style="color:#b45309;font-weight:600;">Due in {} days</span>',
                days,
            )
        return format_html('<span style="color:#15803d;">On track</span>')