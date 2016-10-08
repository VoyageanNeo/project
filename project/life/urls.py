from django.conf.urls import url

from .views import (
    mileStone_create,
    mileStone_detail,
    mileStone_list,
    mileStone_delete,
    mileStory_create,
    mileStory_delete,
    mileStory_detail,
    mileStory_list,
	)

urlpatterns = [
	url(r'^$', mileStory_list, name='storylist'),
    url(r'^create/$', mileStory_create, name='storycreate'),
    url(r'^(?P<story_id>[0-9]+)/$', mileStory_detail, name='storydetail'),
    #TODO make view to edit milestoen
    url(r'^(?P<story_id>[0-9]+)/delete/', mileStory_delete, name='storydelete'),
    url(r'^(?P<story_id>[0-9]+)/createstone/', mileStone_create, name='stonecreate'),
]
