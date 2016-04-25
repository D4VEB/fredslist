from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save

# Ensure that a token is generated and can be used
# to authenticate to the api side.
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return "{}".format(self.title)

class Subcategory(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=100, null=True)

    def __str__(self):
        return "{}, a subcategory of {}".format(self.title, Category.title)

class City(models.Model):
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2, default='NV')

    def __str__(self):
        return "{}".format(self.city)

    # Add unique_together on the city model to make city and state unique
    class Meta:
        unique_together = (("city", "state"),)

class Listing(models.Model):
    title = models.CharField(max_length=100, null=True)
    item_description = models.TextField(max_length=1000, null=True)
    listing_price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    subcategory = models.ForeignKey(Subcategory, null=True)
    email = models.EmailField(max_length=300, null=True)
    phone_number = models.CharField(max_length=10, null=True, blank=True)
    city = models.ForeignKey(City, default='Las Vegas')
    image = models.ImageField(upload_to="listing_images/", null=True, blank=True)
    #TODO: come back to check on this image attribute

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    modified_at = models.DateTimeField(auto_now=True, null=True)

    @property
    def format_date(self):
        """
        https://docs.djangoproject.com/en/1.9/ref/templates/builtins/
        """
        date = self.modified_at
        return "{:%b} {}".format(date, date.day)

    def __str__(self):
        return "{} posted by {}".format(self.title, self.user)

    # Add default_related_name to models instead of multiple custom names on the fields
    class Meta:
        ordering = ["-modified_at"]
        default_related_name = "listings"