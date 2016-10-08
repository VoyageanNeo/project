from __future__ import unicode_literals

from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import pre_save
from django.utils import timezone
from datetime import datetime
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

def upload_location(instance, filename):
    #filebase, extension = filename.split(".")
    #return "%s/%s.%s" %(instance.id, instance.id, extension)
    # PostModel = instance.__class__
    # new_id = PostModel.objects.order_by("id").last().id + 1
    """
    instance.__class__ gets the model Post. We must use this method because the model is defined below.
    Then create a queryset ordered by the "id"s of each object,
    Then we get the last object in the queryset with `.last()`
    Which will give us the most recently created Model instance
    We add 1 to it, so we get what should be the same id as the the post we are creating.
    """
    # return "%s/%s" %(new_id, filename)
    return "%s/%s" % (instance.id, filename)
class UserProfile(models.Model):
    GENRE_CHOICES = (
        ('m', 'Male'),
        ('f', 'Female'),
        ('a', 'Agender'),
        ('b', 'Bigender'),
        ('f', 'Gender-fluid')
    )
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    birth_date = models.DateField(default=datetime.now)
    gender = models.CharField(max_length=1, choices=GENRE_CHOICES)
    # address = models.CharField(max_length=150)
    # postal_code_4 = models.PositiveIntegerField()
    # postal_code_3 = models.PositiveIntegerField()
    # locatity = models.CharField(max_length=30)
    # marital_status = models.CharField(max_length=1, choices=MARITAL_STATUS_CHOICES)
    # child_amount = models.PositiveSmallIntegerField()
    self_introduction = models.TextField(max_length=300, blank=True, null=True)
    image = models.ImageField(upload_to=upload_location,
                              null=True,
                              blank=True,
                              width_field="width_field",
                              height_field="height_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    def __unicode__(self):
        return self.user.username

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse("mileStory:storylist")

class mileStory(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    storyTitle=models.CharField(max_length=20)
    content=models.TextField(max_length=150)
    startDate = models.DateField(auto_now=False, auto_now_add=False, default=datetime.now, blank=True)
    targetDate = models.DateField(auto_now=False, auto_now_add=False, default=datetime.now, blank=True)
    image = models.ImageField(upload_to=upload_location,
                              null=True,
                              blank=True,
                              width_field="width_field",
                              height_field="height_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    # mileStones = models.ForeignKey(mileStone, null=True)


    def __unicode__(self):
        return self.storyTitle

    def __str__(self):
        return self.storyTitle

    def get_absolute_url(self):
        return reverse("mileStory:storydetail", kwargs={"story_id": self.id})

    class Meta:
        ordering = ["-startDate"]
class mileStone(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=120)
    # slug = models.SlugField(unique=True)
    content = models.TextField()
    image = models.ImageField(upload_to=upload_location,
            null=True,
            blank=True,
            width_field="width_field",
            height_field="height_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    IncidentStartDate = models.DateField(auto_now=False, auto_now_add=False, default=datetime.now, blank=True)
    IncidentEndDate = models.DateField(auto_now=False, auto_now_add=False, default=datetime.now, blank=True)

    EMOTION_CHOICES = (
        ('H', 'HAPPY'),
        ('S', 'SAD'),
        ('A','ANGRY'),
        ('J','JOY'),
        ('E', 'EXCITED'),
        ('X', 'ANXIETY'),
        ('B', 'BLUE'),
        ('P', 'PANIC'),
        ('C', 'CHILLING'),
        ('R', 'RELAX'),
    )
    Emotion = models.CharField(max_length=1, choices=EMOTION_CHOICES)
    parentStory = models.ForeignKey(mileStory, on_delete=models.CASCADE)
    # objects = PostManager()

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("mileStory:storydetail", kwargs={"story_id": self.parentStory.id})

    class Meta:
        ordering = ["-IncidentStartDate"]



# def create_slug(instance, new_slug=None):
#     slug = slugify(instance.title)
#     if new_slug is not None:
#         slug = new_slug
#     qs = mileStone.objects.filter(slug=slug).order_by("-id")
#     exists = qs.exists()
#     if exists:
#         new_slug = "%s-%s" %(slug, qs.first().id)
#         return create_slug(instance, new_slug=new_slug)
#     return slug
#
#
# def pre_save_mileStone_receiver(sender, instance, *args, **kwargs):
#     if not instance.slug:
#         instance.slug = create_slug(instance)
#
#
#
# pre_save.connect(pre_save_mileStone_receiver, sender=mileStone)
