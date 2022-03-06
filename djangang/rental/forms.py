from django import forms

from rental.models import Tool, RentalRequest


class ToolSearchForm(forms.Form):
    by_type = forms.ChoiceField(choices=Tool.Type.choices, required=False)
    by_name = forms.CharField(max_length=50, required=False)
    by_brand = forms.CharField(max_length=50, required=False)
    by_price = forms.DecimalField(decimal_places=2, max_digits=7, required=False)


class RentalRequestForm(forms.ModelForm):
    class Meta:
        model = RentalRequest
        fields = ["using_for"]
        labels = {'using_for': "Describe how you will be using the tool, and for how long."}

    def save(self, commit=True):

        return super().save(commit)
