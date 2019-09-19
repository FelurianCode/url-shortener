from django import forms

class UrlForm(forms.Form):
    url = forms.CharField(label='Insert URL:', max_length=200)