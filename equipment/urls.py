from django.urls import path
from . import views

urlpatterns = [
    path('', views.equipment_list, name='equipment_list'),
    path('overdue/', views.equipment_overdue, name='equipment_overdue'),
    path('<int:pk>/', views.equipment_detail, name='equipment_detail'),
]