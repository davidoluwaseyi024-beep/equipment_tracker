from django.urls import path
from . import views

urlpatterns = [
    path("", views.landing_page, name="landing"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("equipment/", views.equipment_list, name="equipment_list"),
    path("overdue/", views.equipment_overdue, name="overdue"),
    path("equipment/<int:pk>/", views.equipment_detail, name="equipment_detail"),
    path("logout/", views.logout_view, name="logout"),
]