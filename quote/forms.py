from django import forms
from home.models import Phone
from django.db import models

class PhoneForm(forms.ModelForm):
	code = models.CharField(max_length=10, primary_key=True)
	name = forms.CharField(max_length=10, help_text='Phone name')
	carrier = models.CharField(max_length=30)
	price = models.IntegerField()
	condition = models.CharField(max_length=8)
	date_listed = models.CharField(max_length=15)
	storage = models.IntegerField()

	class Meta:
		model = Phone
		fields = ('code','name','carrier','price','condition','date_listed','storage')
