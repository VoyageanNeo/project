from __future__ import unicode_literals
from django.db import models
from django.urls import reverse
from django.conf import settings
from django.db.models.signals import pre_save
from django.utils.text import slugify
# from django.contrib.gis.db import models
# Create your models here.
#
# class PostManager(models.Manager):
#     def active(self, *args, **kwargs):
#         # Post.objects.all() = super(PostManager, self).all()
#         return super(PostManager, self).filter(draft=False).filter(publish__lte=timezone.now())


def upload_location(instance, filename):
    # filebase, extension = filename.split(".")
    # return "%s/%s.%s" %(instance.id, instance.id, extension)
    # PersonModel = instance.__class__
    # new_id = PersonModel.objects.order_by("id").last().id + 1
    """
    instance.__class__ gets the model Post. We must use this method because the model is defined below.
    Then create a queryset ordered by the "id"s of each object,
    Then we get the last object in the queryset with `.last()`
    Which will give us the most recently created Model instance
    We add 1 to it, so we get what should be the same id as the the post we are creating.
    """
    return "%s/%s" % (instance.id, filename)


class Person(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    firstname=models.CharField(max_length=30)
    # slug = models.SlugField(unique=True)
    lastname=models.CharField(max_length=30)
    age=models.PositiveSmallIntegerField()
    numberofKids=models.SmallIntegerField(default=0)
    enrolldate=models.DateTimeField(auto_now=True, auto_now_add=False)
    image = models.ImageField(upload_to=upload_location,
                              null=True,
                              blank=True,
                              width_field="width_field",
                              height_field="height_field")
    selfintroduction=models.TextField(default="I started hosting kids !! Let's cooperate her by sending warm greeting card")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)

    def __unicode__(self):
        name = self.firstname + ' ' + self.lastname
        return name
    def __str__(self):
        name = self.firstname + ' ' + self.lastname
        return name
    def get_name(self):
        name = self.firstname + ' ' + self.lastname
        return name
    def get_absolute_url(self):
        return reverse("welcomehome:detail", kwargs={"id": self.id})
    class Meta:
        ordering=["-enrolldate"]


# def create_slug(instance, new_slug=None):
#     slug = slugify(instance.get_name)
#     if new_slug is not None:
#         slug = new_slug
#     qs = Person.objects.filter(slug=slug).order_by("-id")
#     exists = qs.exists()
#     if exists:
#         new_slug = "%s-%s" %(slug, qs.first().id)
#         return create_slug(instance, new_slug=new_slug)
#     return slug
# def pre_save_post_receiver(sender, instance, *args, **kwargs):
#     # if *args is present, it's going to be initialized to tuple
#     # if **kwargs is present, it's going to be initiialize to new dictionary
#     if not instance.slug:
#         instance.slug = create_slug(instance)
#
#
# pre_save.connect(pre_save_post_receiver, sender=Person)
















# class Home(models.Model):
#     geometry = models.PointField(srid=4326)
#     objects = models.GeoManager()
#
#     def __unicode__(self):
#         return '%s %s' % (self.geometry.x, self.geometry.y)
#     def __str__(self):
#         return '%s %s' % (self.geometry.x, self.geometry.y)
# class storyboard(models.Model):