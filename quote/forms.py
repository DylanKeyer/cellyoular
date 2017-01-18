from django import forms
from home.models import Phone
from django.db import models

class PhoneForm(forms.ModelForm):
	name = forms.ModelChoiceField(queryset= Phone.objects.values_list('name').distinct())
	carrier = forms.ModelChoiceField(queryset=Phone.objects.values_list('carrier'))
	condition = forms.ModelChoiceField(queryset=Phone.objects.values_list('condition'))
	storage = forms.ModelChoiceField(queryset=Phone.objects.values_list('storage'))
	class Meta:
		model = Phone
		fields = ('name','carrier','condition','storage')
