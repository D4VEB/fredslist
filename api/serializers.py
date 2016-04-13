from django.contrib.auth.models import User
from rest_framework import serializers
from classifieds.models import Listing, Category, Subcategory, City


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'listings')

class CitySerializer(serializers.ModelSerializer):

    listings = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = City
        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):

    subcategories = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Category
        fields = "__all__"

class SubcategorySerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    listings = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Subcategory
        fields = "__all__"


class ListingSerializer(serializers.ModelSerializer):
    city = CitySerializer(read_only=True)
    subcategory = SubcategorySerializer(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Listing
        fields = "__all__"