from api.views import CategoryDetail, SubcategoryDetail, UserList, UserDetail, \
    CityList, CategoryList, SubCategoryList, CityDetail, ListCreateListing, \
    DetailUpdateDeleteListing
from rest_framework.authtoken import views
from django.conf.urls import url, include

urlpatterns = [
    url(r'^api-token-auth/$', views.obtain_auth_token),
    url(r'^docs/', include('rest_framework_swagger.urls')),
    #url(r'$', UserList.as_view(), name="list_user"),
    url(r'^users/$', UserList.as_view(), name="list_user"),
    url(r'^users/(?P<pk>\d+)/$', UserDetail.as_view(), name="detail_user"),
    url(r'^cities/(?P<pk>\d+)/$', CityDetail.as_view(), name="detail_city"),
    url(r'^cities/$', CityList.as_view(), name="city_list"),
    url(r'^categories/$', CategoryList.as_view(), name="list_category"),
    url(r'^categories/(?P<pk>\d+)/$', CategoryDetail.as_view(), name="detail_category"),
    url(r'^subcategories/$', SubCategoryList.as_view(),
        name="subcategory_list"),
    url(r'^subcategories/(?P<pk>\d+)/$', SubcategoryDetail.as_view(),
        name="subdetail_category"),
    url(r'^classifieds/$', ListCreateListing.as_view(),
        name="list_create_listing"),
    url(r'^classifieds/(?P<pk>\d+)/$', DetailUpdateDeleteListing.as_view(),
        name="detail_update_delete_listing")
]
