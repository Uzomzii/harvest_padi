from django import forms
from .models import EnergyUnit

INPUT = "border border-gray-300 rounded-lg px-3 py-2 w-full"

class EnergyUsageForm(forms.Form):
    # (existing)
    date = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    equipment = forms.CharField()
    kwh = forms.FloatField(min_value=0)
    cost_ngn = forms.FloatField(min_value=0)

# NEW
class EnergyUnitForm(forms.ModelForm):
    class Meta:
        model = EnergyUnit
        fields = ["unit_type", "name", "capacity", "efficiency_pct"]
        widgets = {
            "unit_type": forms.Select(attrs={"class": INPUT, "placeholder": "Select Unit Type"}),
            "name": forms.TextInput(attrs={"class": INPUT, "placeholder": "e.g., Solar Dehydrator Unit 3"}),
            "capacity": forms.TextInput(attrs={"class": INPUT, "placeholder": "e.g., 50 kg/day or 500 kg"}),
            "efficiency_pct": forms.NumberInput(attrs={"class": INPUT, "placeholder": "e.g., 87", "min": 0, "max": 100}),
        }
