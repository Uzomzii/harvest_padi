from django.shortcuts import render, redirect
from django.utils.translation import gettext as _
from .models import FarmerProfile
from .utils import get_role

ROLES = ['farmer','buyer','investor','seller']

def home(request):
    role = request.session.get('role', 'farmer')
    return render(request, 'core/home.html', {'role': role})

def onboarding(request):
    if request.method == 'POST':
        name = request.POST.get('name') or 'Guest'
        role = request.POST.get('role') or 'farmer'
        if role not in ROLES:
            role = 'farmer'
        request.session['name'] = name
        request.session['role'] = role
        return redirect('home')
    return render(request, 'core/onboarding.html', {'roles': ROLES})

def switch_role(request, role):
    if role in ROLES:
        request.session['role'] = role
    return redirect('home')

def farmers(request):
    return render(request, 'core/farmers.html', {
        'role': get_role(request),
        'farmers': FarmerProfile.objects.all()
    })