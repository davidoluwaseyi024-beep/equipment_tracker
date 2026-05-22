from django.db import models
from django.utils import timezone


class Equipment(models.Model):
    class Condition(models.TextChoices):
        GOOD = "good", "Good"
        FAIR = "fair", "Fair"
        POOR = "poor", "Poor"

    class Status(models.TextChoices):
        IN_SERVICE        = "in_service",        "In Service"
        UNDER_MAINTENANCE = "under_maintenance",  "Under Maintenance"
        OUT_OF_SERVICE    = "out_of_service",     "Out of Service"
    name = models.CharField(   #charfied is for short value like name and i use it when i want a short structured with max length
        max_length=200,
        help_text="Full descriptive name, e.g. 'Centrifugal Pump P-101'.",
    )
    serial_number = models.CharField(
        max_length=100,
        unique=True,
        db_index=True,
        help_text="Manufacturer serial number. Must be globally unique.",
    )
    location = models.CharField(
        max_length=200,
        help_text="Current physical location, e.g. 'Lagos Depot - Loading Bay 2'.",
    )
    condition = models.CharField(
        max_length=10,
        choices=Condition.choices,
        default=Condition.GOOD,
        help_text="Physical condition of the equipment.",
    )
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.IN_SERVICE,
        db_index=True,
        help_text="Current operational status.",
    )
    critical = models.BooleanField(
        default=False,
        db_index=True,
        help_text="Mark True for safety- or production-critical equipment.",
    )

    last_service_date = models.DateField(
        null=True,
        blank=True,
        help_text="Date maintenance was last completed.",
    )
    next_due_date = models.DateField(
        null=True,
        blank=True,
        db_index=True,
        help_text="Next scheduled service date. Used for overdue alerts.",
    )
    notes = models.TextField(
        blank=True,
        default="",
        help_text="Additional remarks, fault history, or inspection notes.",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    @property
    def is_overdue(self) -> bool:
        """Returns True if next_due_date is set and in the past."""
        if self.next_due_date is None:
            return False
        return self.next_due_date < timezone.now().date()

    def __str__(self) -> str: #defines how your object should look when printed or shown as text. In Django, /
        # it usually makes the admin panel something readable instead of a generic
        return f"{self.name} ({self.serial_number})"
    class Meta:
        ordering = ["next_due_date"]   # NULLs sort last in most DBs
        verbose_name = "Equipment"
        verbose_name_plural = "Equipment"
        indexes = [
            # Composite index for the most common dashboard query:
            # "show me all critical equipment that is overdue"
            models.Index(fields=["critical", "next_due_date"], name="idx_critical_due"),
        ]
