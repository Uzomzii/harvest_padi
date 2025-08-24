# aihub/views.py
from django.shortcuts import render
from .forms import YieldForm, DiseaseForm
from .ai_logic import estimate_yield, fake_disease_detect
from .models import DiseaseScan

def yield_form(request):
    ctx = {'result': None}
    if request.method == 'POST':
        form = YieldForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            ctx['result'] = estimate_yield(data)
    else:
        form = YieldForm(initial={'crop':'tomato','seedlings_per_hectare':20000,'farm_size_hectares':1.0})
    ctx['form'] = form
    return render(request, 'ai/yield_form.html', ctx)

def disease_form(request):
    ctx = {'result': None}
    if request.method == 'POST':
        form = DiseaseForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            label, conf = fake_disease_detect(image.name)  # e.g., ("Early Blight", 0.92)
            scan = DiseaseScan.objects.create(image=image, result_label=label, confidence=conf)

            # --- UI helpers ----
            pct = round(conf * 100)
            if conf >= 0.85:
                severity = ("High", "text-red-600", "bg-red-50")
            elif conf >= 0.65:
                severity = ("Moderate", "text-orange-600", "bg-orange-50")
            else:
                severity = ("Low", "text-green-600", "bg-green-50")

            RECS = {
                "Early Blight": [
                    "Apply copper-based fungicide",
                    "Improve air circulation around plants",
                    "Remove affected leaves immediately",
                ],
                "Powdery Mildew": [
                    "Use sulfur or potassium bicarbonate spray",
                    "Avoid overhead irrigation; water at soil level",
                    "Thin foliage to reduce humidity",
                ],
                "Leaf Spot": [
                    "Remove and destroy infected leaves",
                    "Apply bio-fungicide (e.g., Bacillus subtilis)",
                    "Rotate crops; avoid night watering",
                ],
                "Healthy": [
                    "Maintain regular scouting",
                    "Keep foliage dry; irrigate in the morning",
                    "Use balanced organic nutrition",
                ],
            }
            actions = RECS.get(label, ["Maintain good field hygiene", "Scout regularly", "Use resistant varieties where possible"])

            ctx['result'] = {
                'id': scan.id,
                'image_url': scan.image.url,
                'label': label,
                'confidence_pct': pct,
                'severity_name': severity[0],
                'severity_text_cls': severity[1],   # text color class
                'severity_bg_cls': severity[2],     # light bg for chip
                'actions': actions,
            }
    else:
        form = DiseaseForm()

    ctx['form'] = form
    return render(request, 'ai/disease_form.html', ctx)
