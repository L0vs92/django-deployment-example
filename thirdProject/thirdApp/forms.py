from django import forms
from django.core import validators


def checkForZ(value):
    if value[0] != "Z":
        raise forms.ValidationError("Needs to start with Z")


class FormFile(forms.Form):
    name = forms.CharField(validators=[checkForZ])
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[
                                 validators.MaxLengthValidator(0)])
