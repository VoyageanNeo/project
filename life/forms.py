from django import forms
from django.utils import timezone
from pagedown.widgets import PagedownWidget
from .models import mileStone, mileStory, UserProfile
from django.contrib.auth.models import User
from cStringIO import StringIO
import os

from django.db import models
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage as storage

from PIL import Image

# Thumbnail size tuple defined in an app-specific settings module - e.g. (400, 400)
from project.settings.base import THUMB_SIZE


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

    def save(self, *args, **kwargs):
        """
        Make and save the thumbnail for the photo here.
        """
        super(image, self).save(*args, **kwargs)
        if not self.make_thumbnail():
            raise Exception('Could not create thumbnail - is the file type valid?')

    def make_thumbnail(self):
        """
        Create and save the thumbnail for the photo (simple resize with PIL).
        """
        fh = storage.open(self.image.name, 'r')
        try:
            image = Image.open(fh)
        except:
            return False
        image.thumbnail(THUMB_SIZE, Image.ANTIALIAS)
        fh.close()
        # Path to save to, name, and extension
        thumb_name, thumb_extension = os.path.splitext(self.image.name)
        thumb_extension = thumb_extension.lower()
        thumb_filename = thumb_name + '_thumb' + thumb_extension
        if thumb_extension in ['.jpg', '.jpeg']:
            FTYPE = 'JPEG'
        elif thumb_extension == '.gif':
            FTYPE = 'GIF'
        elif thumb_extension == '.png':
            FTYPE = 'PNG'
        else:
            return False  # Unrecognized file type
        # Save thumbnail to in-memory file as StringIO
        temp_thumb = StringIO()
        image.save(temp_thumb, FTYPE)
        temp_thumb.seek(0)

        # Load a ContentFile into the thumbnail field so it gets saved
        self.thumbnail.save(thumb_filename, ContentFile(temp_thumb.read()), save=True)
        temp_thumb.close()
        return True


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

