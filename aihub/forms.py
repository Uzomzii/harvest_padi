from django import forms

CROPS = [
    ('tomato', 'Tomato'),
    ('pepper', 'Pepper'),
    ('onion', 'Onion'),
    ('carrot', 'Carrot'),
    ('cabbage', 'Cabbage'),
]

SOIL = [('sandy', 'Sandy'), ('loam', 'Loam'), ('clay', 'Clay')]
IRR = [('rainfed', 'Rain-fed'), ('drip', 'Drip'), ('flood', 'Flood')]

BORDER = 'border border-gray-300 rounded px-3 py-2 w-full'

class YieldForm(forms.Form):
    crop = forms.ChoiceField(
        choices=CROPS,
        widget=forms.Select(attrs={'class': BORDER})
    )
    seedlings_per_hectare = forms.IntegerField(
        min_value=1000, max_value=200000,
        widget=forms.NumberInput(attrs={'class': BORDER})
    )
    farm_size_hectares = forms.FloatField(
        min_value=0.1, max_value=1000,
        widget=forms.NumberInput(attrs={'class': BORDER})
    )
    planting_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': BORDER})
    )
    soil_type = forms.ChoiceField(
        choices=SOIL,
        widget=forms.Select(attrs={'class': BORDER})
    )
    location = forms.CharField(
        help_text="City/LGA/State", required=False,
        widget=forms.TextInput(attrs={'class': BORDER})
    )
    irrigation = forms.ChoiceField(
        choices=IRR,
        widget=forms.Select(attrs={'class': BORDER})
    )
    fertilizer = forms.CharField(
        help_text="Type used or planned", required=False,
        widget=forms.TextInput(attrs={'class': BORDER})
    )

class DiseaseForm(forms.Form):
    image = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={'class': BORDER})
    )
