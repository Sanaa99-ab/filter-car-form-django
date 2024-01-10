# polls/forms.py

from django import forms

class CarSearchForm(forms.Form):
    marque = forms.CharField(max_length=50, required=False)
    modele = forms.CharField(max_length=50, required=False)
    annee = forms.IntegerField(required=False)
    price = forms.DecimalField(required=False)
    
