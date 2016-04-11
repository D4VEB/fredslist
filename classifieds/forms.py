from classifieds.models import Listing
from django import forms

class ListingForm(forms.ModelForm):
    class Meta:

        model = Listing
        fields = ("title", "item_description", "listing_price",
                  "subcategory", "city", "email", "phone_number", "image")

class ListingUpdateForm(forms.ModelForm):

    class Meta:
        model = Listing
        fields = ("title", "item_description", "listing_price",
                  "subcategory", "city", "email", "phone_number", "image")