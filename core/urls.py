from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('onboarding/', views.onboarding, name='onboarding'),
    path('switch-role/<str:role>/', views.switch_role, name='switch_role'),
    path('farmers/', views.farmers, name='farmers'),  # NEW
]
