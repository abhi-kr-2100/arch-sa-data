from django import forms


class DataForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    tilia_template_file = forms.FileField()
