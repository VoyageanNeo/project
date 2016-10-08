from django import forms
from django.utils import timezone
from pagedown.widgets import PagedownWidget
from .models import Signup
from django.db import models
class ContactForm(forms.Form):
    # the argument is different from creating models by modelForm
    email=forms.EmailField()
    full_name=forms.CharField(max_length=60)
    message=forms.CharField(max_length=200)
class SignupForm(forms.ModelForm):
    class Meta:
        model = Signup
        fields = [
            "full_name",
            "email",
        ]
    def clean_email(self):
        # print self.cleaned_data
        email = self.cleaned_data.get('email')
        email_base, provider=email.split('@')
        domain, extension=provider.split('.')
        if not extension=="edu":
            raise forms.ValidationError("Please use a valid college email account")
        return email
    def clean_full_name(self):
        return self.cleaned_data.get("full_name")
