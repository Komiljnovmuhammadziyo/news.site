from django import forms


class ResultForm(forms.Form):
    num1 = forms.IntegerField()
    num2 = forms.IntegerField()
    amal = forms.CharField(max_length=1)
