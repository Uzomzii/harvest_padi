# energy/views.py
from django.shortcuts import render, redirect
from django.db.models import Sum
from datetime import date, timedelta
from .models import RenewableProduct, EnergyUsage, EnergyUnit
from .forms import EnergyUsageForm, EnergyUnitForm
from core.utils import get_role, role_required


def energy_home(request):
    role = get_role(request)
    products = RenewableProduct.objects.all()[:12]

    # Pull last 30 days of usage (farmers see the tracker; others see charts hidden)
    last_day = date.today()
    start_day = last_day - timedelta(days=29)
    usage_qs = EnergyUsage.objects.filter(date__gte=start_day, date__lte=last_day)

    # Aggregate totals
    total_kwh = usage_qs.aggregate(k=Sum('kwh'))['k'] or 0
    total_cost = usage_qs.aggregate(c=Sum('cost_ngn'))['c'] or 0
    avg_cost_per_kwh = round(total_cost / total_kwh, 2) if total_kwh else 0.0

    # Diesel baseline (demo assumption) to show savings
    DIESEL_NGN_PER_KWH = 250  # tweak for your demo
    est_savings = max(DIESEL_NGN_PER_KWH - avg_cost_per_kwh, 0) * total_kwh if total_kwh else 0

    # ---- Time series (group by DateField directly; no TruncDate) ----
    rows = (
        usage_qs.values('date')
        .annotate(kwh=Sum('kwh'))
        .order_by('date')
    )
    day_map = {r['date']: float(r['kwh'] or 0) for r in rows}

    labels, series_kwh = [], []
    for i in range(30):
        d = start_day + timedelta(days=i)
        # Windows-safe label (no %-d); also remove leading zero in day
        labels.append(d.strftime('%b %d').replace(' 0', ' '))
        series_kwh.append(day_map.get(d, 0.0))

    # Equipment breakdown (top 6)
    eq_rows = (
        usage_qs.values('equipment')
        .annotate(kwh=Sum('kwh'))
        .order_by('-kwh')[:6]
    )
    eq_labels = [r['equipment'] for r in eq_rows]
    eq_series = [float(r['kwh'] or 0) for r in eq_rows]

    chart_data = {
        "labels": labels,
        "kwhSeries": series_kwh,
        "equipLabels": eq_labels,
        "equipSeries": eq_series,
    }

    # Recent table (as before) for farmers
    recent_usage = EnergyUsage.objects.order_by('-date')[:10] if role == 'farmer' else []

    ctx = {
        'role': role,
        'products': products,
        'usage': recent_usage,
        'totals': {
            'kwh': round(total_kwh, 2),
            'cost_ngn': round(total_cost, 2),
            'avg_cost_per_kwh': avg_cost_per_kwh,
            'est_savings': round(est_savings, 2),
        },
        'chart_data': chart_data,   # <-- was 'chart_json': json.dumps(chart_data)
        'diesel_ref': DIESEL_NGN_PER_KWH,
    }
    return render(request, 'energy/home.html', ctx)


def energy_usage(request):
    if request.method == 'POST':
        form = EnergyUsageForm(request.POST)
        if form.is_valid():
            EnergyUsage.objects.create(**form.cleaned_data)
            return redirect('energy_home')
    else:
        form = EnergyUsageForm()
    return render(request, 'energy/usage.html', {'form': form})


def energy_unit_new(request):
    if request.method == "POST":
        form = EnergyUnitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('energy_home')
    else:
        form = EnergyUnitForm()
    return render(request, 'energy/unit_form.html', {"form": form})