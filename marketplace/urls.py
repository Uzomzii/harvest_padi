from django.urls import path
from . import views

urlpatterns = [
    path('', views.market_home, name='market_home'),
    path('type/<str:listing_type>/', views.market_list, name='market_list'),

    # Role dash + create
    path('buyer/', views.buyer_dashboard, name='buyer_dashboard'),
    path('buyer/portfolio/new/', views.buyer_portfolio_new, name='buyer_portfolio_new'),

    path('seller/', views.seller_dashboard, name='seller_dashboard'),
    path('seller/listing/new/', views.seller_listing_new, name='seller_listing_new'),

    path('investor/', views.investor_dashboard, name='investor_dashboard'),
]
