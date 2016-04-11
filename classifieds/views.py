from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy, reverse
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, render
from django.utils import timezone
from django.views.generic import ListView, DetailView, \
    UpdateView, DeleteView, CreateView, RedirectView
# from django.core.mail import send_mail
# from django.core.mail import EmailMultiAlternatives
from classifieds.models import Listing, Category, Subcategory, City
from classifieds.forms import ListingForm, ListingUpdateForm


# import logging
#
# logger = logging.getLogger(__name__)

# Create your views here.

def get_city(request):
    city_id = request.session.get("city_id", None)

    if hasattr(request.user, "profile") and hasattr(request.user.profile, "city"):
        return request.user.profile.city
    elif request.session.get("city_id", None):
        return City.objects.get(pk=city_id)
    else:
        return None

def query_sort(get, qs):

    if "price" in get and get["price"] == "lowest":
        qs = qs.order_by("price")
    elif "price" in get and get["price"] == "highest":
        qs = qs.order_by("-price")

    if "modified" in get and get["modified"] == "newest":
        qs = qs.order_by("-modified_time")
    elif "modified" in get and get["modified"] == "oldest":
        qs = qs.order_by("modified_time")

    return qs

class MainPageView(ListView):
    """
    Users will see classifieds from their own city.
    """
    template_name_suffix = '_mainpage'

    def get_queryset(self):
        qs = Listing.objects.all()
        return qs

    def get_context_data(self, **kwargs):
        """

        """
        context = super().get_context_data(**kwargs)
        city = get_city(self.request)

        if city:
            context["city"] = city

        context["cities"] = City.objects.all()
        return context


class CategoryView(ListView):

    template_name = "classifieds/subcategory_list.html"
    context_object_name = "classifieds"
    paginate_by = 10

    def get_queryset(self):
        """
        """
        category = Category.objects.get(pk=self.kwargs["pk"])
        city = get_city(self.request)

        qs = Listing.objects.filter(subcategory__category=category)

        if city:
            qs = qs.filter(city__id=city.id)

        return query_sort(self.request.GET, qs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = Category.objects.get(pk=self.kwargs["pk"])
        context["category"] = category

        view = self.request.GET.get("view", "list")
        context['view'] = view
        return context

class SubcategoryView(ListView):
    template_name_suffix = '_subcategory'
    context_object_name = 'classifieds'
    paginate_by = 10

    def get_queryset(self):
        subcategory = Subcategory.objects.get(pk=self.kwargs["pk"])
        city = get_city(self.request)

        qs = Listing.objects.filter(subcategory=subcategory)

        if city:
            qs = qs.filter(city__id=city.id)

        return query_sort(self.request.GET, qs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = Subcategory.objects.get(pk=self.kwargs["pk"])
        context["category"] = category

        view = self.request.GET.get("view", "list")
        context['view'] = view
        return context

class ListingDetail(DetailView):
    # Fill out template
    model = Listing
    template_name_suffix = '_detail'
    context_object_name = 'listing'


class ListingCreate(CreateView):
    model = Listing
    form_class = ListingForm
    success_url = reverse_lazy("mainpage")
    template_name_suffix = '_create'
    pk_url_kwarg = "id"

    def form_valid(self, form):
        """
        https://docs.djangoproject.com/en/1.9/topics/class-based-views/generic-editing/#models-and-request-user
        """
        if self.request.user.pk:
            form.instance.created_by = self.request.user
            form.instance.city = get_city(self.request)
        return super().form_valid(form)


class ListingUpdate(LoginRequiredMixin, UpdateView):
    model = Listing
    form_class = ListingUpdateForm
    template_name_suffix = "_update"
    success_url = reverse_lazy("mainpage")
    pk_url_kwarg = "id"

class ListingDelete(DeleteView):
    model = Listing
    template_name_suffix = "_delete"
    success_url = reverse_lazy("mainpage")

class AllCityList(ListView):
    model = City
    context_object_name = "cities"
    template_name = "classifieds/cities_combined.html"


class CityRedirect(RedirectView):
    pattern_name = "city_redirect"
    permanent = False

    def get_redirect_url(self, *args, **kwargs):
        chosen_city = get_object_or_404(City, pk=self.kwargs["id"])
        self.request.session["city_id"] = chosen_city.id
        if self.request.user.pk:
            self.request.user.profile.city = chosen_city
            self.request.user.profile.save()
        return reverse("mainpage")


class UserDetail(ListView):
    template_name = "classifieds/user_detail.html"
    context_object_name = "listings"

    def get_queryset(self):
        """
        """
        profiled_user = User.objects.get(pk=self.kwargs['pk'])
        return Listing.objects.filter(user=profiled_user.order_by("-modified_time"))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profiled_user = User.objects.get(pk=self.kwargs['pk'])
        context["profiled_user"] = profiled_user
        context["user_match"] = self.request.user == profiled_user
        return context