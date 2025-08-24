from django.urls import path
from . import views

urlpatterns = [
    path('', views.energy_home, name='energy_home'),
    path('usage/', views.energy_usage, name='energy_usage'),
    # NEW:
    path('unit/new/', views.energy_unit_new, name='energy_unit_new'),
]
