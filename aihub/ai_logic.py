# Demo-only "AI" logic with simple rules-of-thumb

from datetime import date, timedelta

# Days to maturity (rough demo values)
MATURITY_DAYS = {
    'tomato': 80,
    'pepper': 100,
    'onion': 120,
    'carrot': 90,
    'cabbage': 110,
}

# kg per plant baseline (very rough demo figures)
BASE_YIELD_PER_PLANT = {
    'tomato': 2.5,
    'pepper': 1.2,
    'onion': 0.3,
    'carrot': 0.2,
    'cabbage': 1.5,
}

# price per kg by crop (₦)
PRICE_PER_KG = {
    'tomato': 800,
    'pepper': 1200,
    'onion': 700,
    'carrot': 900,
    'cabbage': 600,
}

SOIL_FACTOR = {'sandy': 0.9, 'loam': 1.1, 'clay': 0.95}
IRR_FACTOR = {'rainfed': 0.9, 'drip': 1.15, 'flood': 1.0}

def estimate_yield(form_data):
    crop = form_data['crop']
    spph = int(form_data['seedlings_per_hectare'])
    size = float(form_data['farm_size_hectares'])
    soil = form_data['soil_type']
    irr = form_data['irrigation']
    plant_date = form_data['planting_date']

    per_plant = BASE_YIELD_PER_PLANT.get(crop, 1.0)
    soil_k = SOIL_FACTOR.get(soil, 1.0)
    irr_k = IRR_FACTOR.get(irr, 1.0)

    total_plants = spph * size
    total_kg = total_plants * per_plant * soil_k * irr_k
    price = PRICE_PER_KG.get(crop, 500)
    value_ngn = total_kg * price

    maturity = MATURITY_DAYS.get(crop, 90)
    harvest_date = plant_date + timedelta(days=maturity)

    return {
        'expected_yield_kg': round(total_kg, 2),
        'expected_value_ngn': round(value_ngn, 2),
        'expected_harvest_date': harvest_date,
        'market_price_per_kg': price,
        'assumptions': {
            'yield_per_plant_kg': per_plant,
            'soil_factor': soil_k,
            'irrigation_factor': irr_k,
            'days_to_maturity': maturity,
        }
    }

def fake_disease_detect(file_name:str):
    # Simple stub: classify by filename keywords for demo
    name = file_name.lower()
    if 'blight' in name:
        return ('Early Blight', 0.92)
    if 'mildew' in name:
        return ('Powdery Mildew', 0.88)
    if 'leaf' in name:
        return ('Leaf Spot', 0.81)
    return ('Healthy', 0.75)
