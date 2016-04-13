from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView


from user_profiles.models import UserProfile

class RegisteredUser(CreateView):

    model = User
    form_class = UserCreationForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("listing_mainpage")

    def form_valid(self, form):
        response = super().form_valid(form)
        UserProfile.objects.create(user=self.object)
        return response
