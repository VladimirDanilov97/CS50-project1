from django import forms
from django.forms.widgets import TextInput, Textarea

class CreateNewPage(forms.Form):
    title = forms.CharField(max_length=120, min_length=1, widget=TextInput(attrs={'class':'input-group-text'}))
    content = forms.CharField(widget=Textarea(attrs={'class':'input-group-text'}))
