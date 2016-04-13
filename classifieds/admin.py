from django.contrib import admin
# Register your models here.
from gunicorn.config import User

from classifieds.models import Listing, Category, Subcategory, City

@admin.register(Listing)
class ClassifiedsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'item_description', 'listing_price',
                    'subcategory', 'city', 'created_at', 'modified_at')
    readonly_fields = ('created_at', 'modified_at')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category')


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'city')

