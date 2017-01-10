from django.db import models

# Create your models here.
class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    address1 = models.CharField(max_length=95, blank=True)
    address2 = models.CharField(max_length=35, blank=True)
    city = models.CharField(max_length=35, blank=True)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username