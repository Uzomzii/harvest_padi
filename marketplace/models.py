from django.db import models

LISTING_TYPES = [
    ('produce', 'Produce'),   # for Farmers to sell harvest
    ('input', 'Input'),       # for Sellers: seeds, fertilizer, tools
    ('investment', 'Investment'), # for Investors: offers/loans
    ('rfq', 'RFQ'),           # for Buyers: request for quotation
]

class Listing(models.Model):
    title = models.CharField(max_length=200)
    listing_type = models.CharField(max_length=20, choices=LISTING_TYPES)
    category = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=100, blank=True)
    quantity = models.CharField(max_length=100, blank=True)
    price_text = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='market/', blank=True, null=True)
    description = models.TextField(blank=True)
    is_verified = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.get_listing_type_display()})"


class BuyerPortfolio(models.Model):
    title = models.CharField(max_length=200)
    produce = models.CharField(max_length=100)  # e.g., tomato
    quantity = models.CharField(max_length=100) # e.g., 5 tons
    location = models.CharField(max_length=100, blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
