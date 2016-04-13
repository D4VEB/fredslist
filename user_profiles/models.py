from django.contrib.auth.models import User
from django.db import models

from classifieds.models import City


class UserProfile(models.Model):

    user = models.OneToOneField(User, null=True)
    city = models.ForeignKey(City, null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.user)