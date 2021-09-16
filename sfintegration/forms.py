from django import forms

class ArrayForm(forms.Form):
    array1 = forms.CharField(required=True)
    array2 = forms.CharField(required=True)