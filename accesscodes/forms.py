from django import forms
from django.utils.safestring import mark_safe
from django.forms.widgets import HiddenInput


class GetCodeForm(forms.Form):
    user_email = forms.EmailField(label=mark_safe('<strong>e-mail:</strong>'), max_length=100)
    user_name = forms.CharField(label='uživatelské jméno:', max_length=100, 
        required=False, widget = forms.HiddenInput())
    firstname = forms.CharField(label='křestní jméno:', max_length=100, 
        required=False)
    surname = forms.CharField(label='příjmení:', max_length=100, 
        required=False)
    choice_field = forms.ChoiceField(widget=forms.RadioSelect, choices=(), label="")

