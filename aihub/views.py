from django.shortcuts import render
from .forms import YieldForm, DiseaseForm
from .ai_logic import estimate_yield, fake_disease_detect
from .models import DiseaseScan
from core.utils import role_required

@role_required('farmer')
def yield_form(request):
    ctx = {'result': None}
    if request.method == 'POST':
        form = YieldForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            result = estimate_yield(data)
            ctx['result'] = result
    else:
        form = YieldForm(initial={'crop':'tomato', 'seedlings_per_hectare':20000, 'farm_size_hectares':1.0})
    ctx['form'] = form
    return render(request, 'ai/yield_form.html', ctx)

@role_required('farmer')
def disease_form(request):
    ctx = {'result': None}
    if request.method == 'POST':
        form = DiseaseForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            label, conf = fake_disease_detect(image.name)
            scan = DiseaseScan.objects.create(image=image, result_label=label, confidence=conf)
            ctx['result'] = {'label': label, 'confidence': round(conf, 2), 'id': scan.id, 'image_url': scan.image.url}
    else:
        form = DiseaseForm()
    ctx['form'] = form
    return render(request, 'ai/disease_form.html', ctx)
