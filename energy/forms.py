from django import forms

class EnergyUsageForm(forms.Form):
    date = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    equipment = forms.CharField()
    kwh = forms.FloatField(min_value=0)
    cost_ngn = forms.FloatField(min_value=0)
