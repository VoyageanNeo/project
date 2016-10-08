from django import forms
from.models import Person
from django import forms
from django.forms.extras.widgets import SelectDateWidget



class PersonForm(forms.ModelForm):
    class Meta:
        model=Person
        fields=[
            "firstname",
            "lastname",
            "age",
            "numberofKids",
            "image",
        ]