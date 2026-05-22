from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from .models import Equipment


def landing_page(request):
    if request.user.is_authenticated:
        return redirect("dashboard")

    error = None

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("dashboard")
        else:
            error = "Invalid username or password."

    return render(request, "equipment/landing.html", {"error": error})


@login_required
def dashboard(request):
    today = timezone.now().date()

    total_equipment = Equipment.objects.count()
    overdue_equipment = Equipment.objects.filter(next_due_date__lt=today).count()
    due_soon_equipment = Equipment.objects.filter(next_due_date=today).count()
    recent_items = Equipment.objects.all().order_by("next_due_date")[:5]
    in_status_condition_in_service = Equipment.objects.filter(status="in_service").count()
    in_status_condition_under_maintenance = Equipment.objects.filter(status="under_maintenance").count()
    in_status_condition_out_of_service = Equipment.objects.filter(status="out_of_service").count()
    in_condition_good = Equipment.objects.filter(condition="good").count()
    in_condition_fair = Equipment.objects.filter(condition="fair").count()
    in_condition_poor = Equipment.objects.filter(condition="poor").count()


    context = {
        "total_equipment": total_equipment,
        "overdue_equipment": overdue_equipment,
        "due_soon_equipment": due_soon_equipment,
        "recent_items": recent_items,
        "page_title": "Dashboard",
        "in_status_condition_in_service": in_status_condition_in_service,
        "in_status_condition_under_maintenance": in_status_condition_under_maintenance,
        "in_status_condition_out_of_service": in_status_condition_out_of_service,
        "in_condition_good": in_condition_good,
        "in_condition_fair": in_condition_fair,
        "in_condition_poor": in_condition_poor,
    }
    return render(request, "equipment/dashboard.html", context)


@login_required
def equipment_list(request):
    equipments = Equipment.objects.all().order_by("next_due_date")

    context = {
        "equipments": equipments,
        "page_title": "All Equipment",
        "is_overdue_view": False,
    }
    return render(request, "equipment/equipment_list.html", context)


@login_required
def equipment_detail(request, pk):
    equipment = get_object_or_404(Equipment, pk=pk)

    context = {
        "equipment": equipment,
        "page_title": equipment.name,
    }
    return render(request, "equipment/equipment_detail.html", context)


@login_required
def equipment_overdue(request):
    today = timezone.now().date()

    equipments = Equipment.objects.filter(next_due_date__lt=today).order_by("next_due_date")

    context = {
        "equipments": equipments,
        "page_title": "Overdue Equipment",
        "is_overdue_view": True,
    }
    return render(request, "equipment/equipment_list.html", context)


def logout_view(request):
    logout(request)
    return redirect("landing")


