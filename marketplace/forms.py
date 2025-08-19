from django import forms
from .models import Listing, BuyerPortfolio

class BuyerPortfolioForm(forms.ModelForm):
    class Meta:
        model = BuyerPortfolio
        fields = ['title','produce','quantity','location','notes']

class SellerListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ['title','category','location','quantity','price_text','description','image']
    # listing_type is enforced in the view as 'input'
