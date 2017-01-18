from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    address1 = models.CharField(max_length=95, blank=True)
    address2 = models.CharField(max_length=35, blank=True)
    city = models.CharField(max_length=35, blank=True)
    zip_code = models.CharField(max_length=5)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username