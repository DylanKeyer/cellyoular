from django import forms

class Carrier(forms.Form):
    carrier = forms.CharField(label='Carrier', max_length=100)