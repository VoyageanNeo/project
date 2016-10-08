from django import forms
from django.utils import timezone
from pagedown.widgets import PagedownWidget
from .models import mileStone, mileStory

class mileStoryForm(forms.ModelForm):
    class Meta:
        model = mileStory
        fields=[
            'storyTitle',
            'startDate',
            'targetDate',
            'content',
        ]

class mileStoneForm(forms.ModelForm):
    # content=forms.CharField(widget=PagedownWidget)
    # IncidentStartDate= forms.DateField(widget=forms.SelectDateWidget, initial=timezone.now())
    # IncidentEndDate= forms.DateField(widget=forms.SelectDateWidget, initial=timezone.now())
    parentStory = forms.ModelChoiceField(
        queryset=mileStory.objects.all(),
        widget=forms.RadioSelect,
        empty_label='None'
    )
    class Meta:
        model = mileStone
        fields = [
            "title",
            "content",
            "image",
            "IncidentStartDate",
            "IncidentEndDate",
            "Emotion",
            "parentStory"
        ]

