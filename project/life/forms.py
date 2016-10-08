from django import forms
from django.utils import timezone
from pagedown.widgets import PagedownWidget
from .models import mileStone


class mileStoneForm(forms.ModelForm):
    # content=forms.CharField(widget=PagedownWidget)
    publish = forms.DateField(widget=forms.SelectDateWidget, initial=timezone.now())
    class Meta:
        model = mileStone
        fields = [
            "title",
            "content",
            "image",
            "IncidentStartDate",
            "IncidentEndDate",
            "Emotion",
        ]
