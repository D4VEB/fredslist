from django.conf.urls import url
from classifieds.views import ListingDetail, ListingCreate, \
    ListingUpdate, ListingDelete, StripeSubmit

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', ListingDetail.as_view(),
        name="listing_detail"),
    url(r'^create/$', ListingCreate.as_view(),
        name="listing_create"),
    url(r'^update/(?P<id>\d+)/$', ListingUpdate.as_view(),
        name="listing_update"),
    url(r'^delete/(?P<pk>\d+)/$',ListingDelete.as_view(),
        name="listing_delete"),
    url(r'^listing-donate/$', StripeSubmit,
        name = 'chirp_donate')
    ]