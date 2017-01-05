from django import forms
<<<<<<< HEAD
from .models import Quote
from django import models

class QuoteForm(models.ModelForm):
	pass
=======

class Carrier(forms.Form):
    carrier = forms.CharField(label='Carrier', max_length=100)
>>>>>>> 2610830762e31ade50ff7d770a207c8853ce252f
