from django import forms

from .models import Quote
from django import models

class QuoteForm(models.ModelForm):
	pass


class Carrier(forms.Form):
    carrier = forms.CharField(label='Carrier', max_length=100)

