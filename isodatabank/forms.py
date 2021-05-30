from django import forms


class DataForm(forms.Form):
    tilia_template_file = forms.FileField()
