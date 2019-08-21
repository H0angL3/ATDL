from django import forms

class wordProcessForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea)
