from django import forms
from django.utils import timezone
from pagedown.widgets import PagedownWidget
from .models import mileStone, mileStory, UserProfile
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "email"]
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            "birth_date",
            "gender",
            "self_introduction",
            "image",
        ]

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

