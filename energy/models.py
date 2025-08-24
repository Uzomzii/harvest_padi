from django.db import models

class RenewableProduct(models.Model):
    title = models.CharField(max_length=200)
    vendor = models.CharField(max_length=100, blank=True)
    product_type = models.CharField(max_length=100)  # dehydrator, cold_storage, solar_pump
    capacity = models.CharField(max_length=100, blank=True)
    price_text = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

class EnergyUsage(models.Model):
    date = models.DateField()
    equipment = models.CharField(max_length=100)  # e.g., solar_pump_3hp
    kwh = models.FloatField()
    cost_ngn = models.FloatField()

    def __str__(self):
        return f"{self.date} - {self.equipment}"


class EnergyUnit(models.Model):
    UNIT_TYPES = [
        ("cold_storage", "Cold Storage"),
        ("dehydrator", "Solar Dehydrator"),
        ("solar_pump", "Solar Pump"),
        ("other", "Other"),
    ]
    unit_type = models.CharField(max_length=30, choices=UNIT_TYPES)
    name = models.CharField(max_length=120)                     # e.g., “Solar Dehydrator Unit 3”
    capacity = models.CharField(max_length=100, blank=True)     # e.g., “50 kg/day” or “500 kg”
    efficiency_pct = models.PositiveIntegerField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_unit_type_display()} — {self.name}"