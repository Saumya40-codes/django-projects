from django import forms

class CreateNewList(forms.Form):
    name = forms.CharField(max_length=300,label="Name",required=True)
    check = forms.BooleanField()
