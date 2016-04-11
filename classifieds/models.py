from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return "{}".format(self.title)

class Subcategory(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=100, null=True)

    def __str__(self):
        return "{}, a subcategory of {}".format(self.title, self.category.title)
        # simplify the above string if "self.category.title" is wrong

class City(models.Model):
    city = models.CharField(max_length=100)

    def __str__(self):
        return "{}".format(self.city)

class Listing(models.Model):
    title = models.CharField(max_length=100, null=True)
    item_description = models.TextField(max_length=1000, null=True)
    listing_price = models.FloatField(null=True, blank=True)
    subcategory = models.ForeignKey(Subcategory, null=True)
    user = models.ForeignKey(User, null=True, blank=True)
    email = models.EmailField(max_length=300, null=True)
    phone_number = models.CharField(max_length=10, null=True, blank=True)
    city = models.ForeignKey(City, null=True)
    image = models.ImageField(upload_to="listing_images/", null=True, blank=True)
    #TODO: come back to check on this image attribute

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    modified_at = models.DateTimeField(auto_now=True, null=True)

    @property
    def format_date(self):
        """
        https://docs.djangoproject.com/en/1.9/ref/templates/builtins/
        """
        date = self.modified_time
        return "{:%b} {}".format(date, date.day)

    def __str__(self):
        return "{} posted by {}".format(self.title, self.user)