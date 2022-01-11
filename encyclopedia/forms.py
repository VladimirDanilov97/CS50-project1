from django import forms
from django.forms.widgets import TextInput, Textarea

class CreateNewPage(forms.Form):
    title = forms.CharField(initial='', widget=TextInput(attrs={'class':'input-group-text'}))
    content = forms.CharField(initial='', widget=Textarea(attrs={'class':'input-group-text'}))
    