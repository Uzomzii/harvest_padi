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
