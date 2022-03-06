from django import forms

from rental.models import Tool


class ToolSearchForm(forms.Form):
    by_type = forms.ChoiceField(choices=Tool.Type.choices, required=False)
    by_name = forms.CharField(max_length=50, required=False)
    by_brand = forms.CharField(max_length=50, required=False)
    by_price = forms.DecimalField(decimal_places=2, max_digits=7, required=False)
