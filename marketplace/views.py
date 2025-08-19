from django.shortcuts import render, redirect
from .models import Listing, BuyerPortfolio
from .forms import BuyerPortfolioForm, SellerListingForm
from core.utils import get_role, role_required
from core.models import FarmerProfile
from energy.models import RenewableProduct

def market_home(request):
    role = get_role(request)
    # Redirect users straight to their role dashboard
    if role == 'buyer':
        return redirect('buyer_dashboard')
    if role == 'seller':
        return redirect('seller_dashboard')
    if role == 'investor':
        return redirect('investor_dashboard')
    # Farmers can see the full marketplace landing
    sections = []
    for slug, title in [("produce","Produce"),("input","Inputs"),("investment","Investments"),("rfq","RFQs")]:
        items = Listing.objects.filter(listing_type=slug)[:6]
        sections.append({"slug": slug, "title": title, "items": items})
    return render(request, "market/home.html", {"sections": sections, "role": role})

def market_list(request, listing_type):
    qs = Listing.objects.filter(listing_type=listing_type)
    return render(request, 'market/list.html', {'items': qs, 'listing_type': listing_type})

# BUYER: see farmers + create portfolio
@role_required('buyer')
def buyer_dashboard(request):
    return render(request, 'market/buyer_dashboard.html', {
        'farmers': FarmerProfile.objects.all(),
        'portfolios': BuyerPortfolio.objects.order_by('-created_at')[:20],
    })

@role_required('buyer')
def buyer_portfolio_new(request):
    if request.method == 'POST':
        form = BuyerPortfolioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('buyer_dashboard')
    else:
        form = BuyerPortfolioForm()
    return render(request, 'market/buyer_portfolio_form.html', {'form': form})

# SELLER: see farmers + create INPUT listing
@role_required('seller')
def seller_dashboard(request):
    inputs = Listing.objects.filter(listing_type='input').order_by('-created_at')[:20]
    return render(request, 'market/seller_dashboard.html', {
        'farmers': FarmerProfile.objects.all(),
        'inputs': inputs,
    })

@role_required('seller')
def seller_listing_new(request):
    if request.method == 'POST':
        form = SellerListingForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.listing_type = 'input'      # enforce
            obj.is_verified = True          # demo
            obj.save()
            return redirect('seller_dashboard')
    else:
        form = SellerListingForm()
    return render(request, 'market/seller_listing_form.html', {'form': form})

# INVESTOR: see farmers + renewable energy + create investment profile (placeholder)
@role_required('investor')
def investor_dashboard(request):
    return render(request, 'market/investor_dashboard.html', {
        'farmers': FarmerProfile.objects.all(),
        'energy_products': RenewableProduct.objects.all()[:20],
    })
