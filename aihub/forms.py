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

NIGERIA_STATES = [
    ('Abia','Abia'), ('Adamawa','Adamawa'), ('Akwa Ibom','Akwa Ibom'),
    ('Anambra','Anambra'), ('Bauchi','Bauchi'), ('Bayelsa','Bayelsa'),
    ('Benue','Benue'), ('Borno','Borno'), ('Cross River','Cross River'),
    ('Delta','Delta'), ('Ebonyi','Ebonyi'), ('Edo','Edo'),
    ('Ekiti','Ekiti'), ('Enugu','Enugu'), ('Gombe','Gombe'),
    ('Imo','Imo'), ('Jigawa','Jigawa'), ('Kaduna','Kaduna'),
    ('Kano','Kano'), ('Katsina','Katsina'), ('Kebbi','Kebbi'),
    ('Kogi','Kogi'), ('Kwara','Kwara'), ('Lagos','Lagos'),
    ('Nasarawa','Nasarawa'), ('Niger','Niger'), ('Ogun','Ogun'),
    ('Ondo','Ondo'), ('Osun','Osun'), ('Oyo','Oyo'),
    ('Plateau','Plateau'), ('Rivers','Rivers'), ('Sokoto','Sokoto'),
    ('Taraba','Taraba'), ('Yobe','Yobe'), ('Zamfara','Zamfara'),
    ('FCT','FCT (Abuja)'),
]

FERTILIZER_CHOICES = [
    ('synthetic', 'Synthetic (Chemical) Fertilizers'),
    ('mixed', 'Synthetic + Organic (Integrated)'),
]

ORGANIC_FERTILIZERS = [
    ('compost','Compost'),
    ('vermicompost','Vermicompost'),
    ('farmyard_manure','Farmyard manure'),
    ('poultry_manure','Poultry manure (pelletized)'),
    ('green_manure','Green manure'),
    ('bone_meal','Bone meal'),
    ('blood_meal','Blood meal'),
    ('fish_emulsion','Fish emulsion'),
    ('seaweed_kelp','Seaweed / kelp extract'),
    ('neem_cake','Neem cake'),
    ('castor_cake','Castor cake'),
    ('cocoa_pod_compost','Cocoa pod compost'),
    ('biochar','Biochar'),
    ('rock_phosphate','Rock phosphate (organically permitted mineral)'),
    ('sulphate_of_potash','Sulfate of potash (SOP, organic grade)'),
    ('wood_ash','Wood ash (use sparingly)'),
    ('bat_guano','Bat guano'),
]

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

    # ▼ NEW: Nigerian states dropdown
    location = forms.ChoiceField(
        choices=[('', 'Select State')] + NIGERIA_STATES,
        widget=forms.Select(attrs={'class': BORDER})
    )

    irrigation = forms.ChoiceField(
        choices=IRR,
        widget=forms.Select(attrs={'class': BORDER})
    )

    fertilizer = forms.ChoiceField(
        choices=[('', 'Select Fertilizer Type')] 
                + FERTILIZER_CHOICES 
                + ORGANIC_FERTILIZERS,
        required=False,
        widget=forms.Select(attrs={'class': BORDER})
    )


class DiseaseForm(forms.Form):
    image = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={'class': BORDER})
    )
