from django import forms

from rental.models import Tool


class ToolSearchForm(forms.Form):
    by_type = forms.ChoiceField(choices=Tool.Type.choices, required=False)
