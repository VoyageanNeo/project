from __future__ import unicode_literals
from django.db import models

class Contact(models.Model):
    full_name = models.TextField()
    email = models.EmailField()
    message = models.TextField()


class Signup(models.Model):
    email=models.EmailField()
    full_name=models.CharField(max_length=50, default='', null=True)
    timestamp=models.DateField(auto_now_add=True, auto_now=False)
    updated=models.DateField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.full_name
    def __str__(self):
        return self.full_name