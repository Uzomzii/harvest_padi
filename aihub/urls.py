from django.urls import path
from . import views

urlpatterns = [
    path('yield/', views.yield_form, name='yield_form'),
    path('disease/', views.disease_form, name='disease_form'),
]
