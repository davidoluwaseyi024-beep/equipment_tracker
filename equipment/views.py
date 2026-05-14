from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from .models import Equipment


def equipment_list(request):
    equipments = Equipment.objects.all().order_by("next_due_date")

    context = {
        "equipments": equipments,
        "page_title": "All Equipment",
    }
    return render(request, "equipment/equipment_list.html", context)


def equipment_detail(request, pk):
    equipment = get_object_or_404(Equipment, pk=pk)

    context = {
        "equipment": equipment,
        "page_title": equipment.name,
    }
    return render(request, "equipment/equipment_detail.html", context)


def equipment_overdue(request):
    today = timezone.now().date()

    equipments = Equipment.objects.filter(next_due_date__lt=today).order_by("next_due_date")

    context = {
        "equipments": equipments,
        "page_title": "Overdue Equipment",
        "is_overdue_view": True,
    }
    return render(request, "equipment/equipment_list.html", context)