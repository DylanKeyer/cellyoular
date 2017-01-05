from django.db import models

# Create your models here.
class Quote(models.Model):
    name = models.CharField(max_length=100, unique=True)
    carrier = models.CharField(max_length=30)
    quote = models.IntegerField()
    condition = models.CharField(max_length=8)
    storage = models.IntegerField()

    def __str__(self):  #For Python 2, use __str__ on Python 3
        return self.name