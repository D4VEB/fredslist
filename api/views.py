from django.contrib.auth.models import User
from django.views.generic import View
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from classifieds.models import Category, City, Subcategory, Listing
from api.permissions import IsOwnerOrReadOnly
from api.serializers import CategorySerializer, CitySerializer, \
    SubcategorySerializer, ListingSerializer, UserSerializer
from rest_framework.authtoken.models import Token


class TenResultsPaginator(PageNumberPagination):
    page_size = 10

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CityList(generics.ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

class CityDetail(generics.RetrieveAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer

class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

class CategoryDetail(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class SubCategoryList(generics.ListAPIView):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

class SubcategoryDetail(generics.RetrieveAPIView):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer

class ListCreateListing(generics.ListCreateAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    pagination_class = TenResultsPaginator
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        qs = super().get_queryset()

        return qs

class DetailUpdateDeleteListing(generics.RetrieveUpdateDestroyAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    permission_classes = (IsOwnerOrReadOnly,)




