from django.contrib import admin
from .models import Listing
@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ('title','listing_type','location','is_verified','created_at')
    list_filter = ('listing_type','is_verified')
    search_fields = ('title','description','location')
