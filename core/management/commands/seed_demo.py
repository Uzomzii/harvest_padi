from django.core.management.base import BaseCommand
from marketplace.models import Listing
from energy.models import RenewableProduct, EnergyUsage
from datetime import date, timedelta
from core.models import FarmerProfile
import random

class Command(BaseCommand):
    help = "Seed demo data for HarvestPadi"

    def handle(self, *args, **kwargs):
        if Listing.objects.exists():
            self.stdout.write(self.style.WARNING("Listings already exist, skipping."))
        else:
            Listing.objects.create(title="Tomato crates (Grade A)", listing_type="produce", category="tomato",
                location="Kano", quantity="200 crates", price_text="₦10,000/crate", description="Fresh tomatoes ready in 2 weeks.")
            Listing.objects.create(title="Organic Pepper (bulk)", listing_type="produce", category="pepper",
                location="Kaduna", quantity="5 tons", price_text="₦1,100/kg", description="Hot pepper, sorted.")
            Listing.objects.create(title="Hybrid Tomato Seeds", listing_type="input", category="seeds",
                location="Abuja", quantity="500 packs", price_text="₦3,500/pack", description="High yield hybrid.")
            Listing.objects.create(title="Drip Irrigation Kit", listing_type="input", category="irrigation",
                location="Ibadan", quantity="50 kits", price_text="₦120,000/kit", description="Complete set for 1ha.")
            Listing.objects.create(title="Buyer RFQ: Onion 10 tons", listing_type="rfq", category="onion",
                location="Lagos", quantity="10 tons", price_text="Best offer", description="Agro-processor needs onions.")
            Listing.objects.create(title="Investor offer: ₦5m @ 12%", listing_type="investment", category="loan",
                location="Lagos", quantity="Tenor 6 months", price_text="12% APR", description="Working capital for harvest.")
            self.stdout.write(self.style.SUCCESS("Seeded marketplace listings."))

        if RenewableProduct.objects.exists():
            self.stdout.write(self.style.WARNING("Renewable products already exist, skipping."))
        else:
            RenewableProduct.objects.create(title="Solar Dehydrator SD-200", vendor="SunAgro Ltd",
                product_type="dehydrator", capacity="200kg/day", price_text="₦2,500,000", description="Preserve tomatoes post-harvest.")
            RenewableProduct.objects.create(title="Solar Cold Room CR-10", vendor="CoolSun",
                product_type="cold_storage", capacity="10 tons", price_text="₦18,000,000", description="Village-level cold storage.")
            RenewableProduct.objects.create(title="Solar Pump 3HP", vendor="GreenPump",
                product_type="solar_pump", capacity="3 HP", price_text="₦1,150,000", description="Efficient irrigation.")
            self.stdout.write(self.style.SUCCESS("Seeded renewable products."))

        if EnergyUsage.objects.exists():
            self.stdout.write(self.style.WARNING("Energy usage already exists, skipping."))
        else:
            base = date.today()
            for i in range(0, 30):
                d = base - timedelta(days=i)
                # two equipments to make the chart nicer
                k1 = 4.0 + i * 0.15
                k2 = 2.5 + (i % 5) * 0.3
                EnergyUsage.objects.create(date=d, equipment="solar_pump_3hp", kwh=k1, cost_ngn=k1*120)
                EnergyUsage.objects.create(date=d, equipment="cold_room_cr10", kwh=k2, cost_ngn=k2*110)
            self.stdout.write(self.style.SUCCESS("Seeded 30 days of energy usage."))
        # Products
        products = [
            dict(title="Solar Dehydrator SD-200", vendor="SunAgro Ltd", product_type="dehydrator",
                capacity="200kg/day", price_text="2,500,000",
                description="Preserve tomatoes post-harvest."),
            dict(title="Solar Cold Room CR-10", vendor="CoolSun", product_type="cold_storage",
                capacity="10 tons", price_text="18,000,000",
                description="Village-level cold storage."),
            dict(title="Solar Pump 3HP", vendor="GreenPump", product_type="solar_pump",
                capacity="3 HP", price_text="1,150,000",
                description="Efficient irrigation."),
        ]
        for p in products:
            RenewableProduct.objects.get_or_create(title=p["title"], defaults=p)

        # Usage (reset & seed 30 days)
        EnergyUsage.objects.all().delete()
        today = date.today()
        for i in range(30):
            d = today - timedelta(days=i)
            k1 = round(4.0 + (29 - i) * 0.12, 2)             # solar_pump_3hp trend
            k2 = round(2.2 + ((i % 5) * 0.25), 2)            # cold_room_cr10 rhythm
            EnergyUsage.objects.create(date=d, equipment="solar_pump_3hp", kwh=k1, cost_ngn=round(k1 * 120, 2))
            EnergyUsage.objects.create(date=d, equipment="cold_room_cr10", kwh=k2, cost_ngn=round(k2 * 110, 2))

        self.stdout.write(self.style.SUCCESS("Seeded energy products and 30 days of usage."))