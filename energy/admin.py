from django.contrib import admin
from .models import RenewableProduct, EnergyUsage, EnergyUnit

admin.site.register(RenewableProduct)
admin.site.register(EnergyUsage)

@admin.register(EnergyUnit)
class EnergyUnitAdmin(admin.ModelAdmin):
    list_display = ("name", "unit_type", "capacity", "efficiency_pct", "is_active", "created_at")
    list_filter = ("unit_type", "is_active")
    search_fields = ("name", "capacity")
