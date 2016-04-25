from django.contrib import admin
from classifieds.models import Listing, Category, Subcategory, City

@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'item_description', 'listing_price',
                    'subcategory', 'city', 'created_at', 'modified_at')
    readonly_fields = ('created_at', 'modified_at')
    # Add filters for posts for date and city
    list_filter = ['created_at', 'city']
    # Add a search function on the admin that will search through all ads
    search_fields = ['title', 'item_description']

    # Add a custom action for the ads that will allow multiple to be archived
    actions = ['archive_listings']

    def archive_listings(self, request, queryset):
        queryset.update(archived=True)
    archive_listings.short_description = "Archive Listings"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category')


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'city')

