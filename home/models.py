from django.db import models

# Create your models here.
class Phone(models.Model):
    name = models.CharField(max_length=100, unique=True)
    carrier = models.CharField(max_length=30)
    price = models.IntegerField()
    condition = models.CharField(max_length=8)
    date_listed = models.CharField(max_length=15)
    storage = models.IntegerField()

    def __str__(self):  #For Python 2, use __str__ on Python 3
        return self.name