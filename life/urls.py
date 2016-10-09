from django.conf.urls import url

from .views import (
# milestone
    mileStone_create,
    mileStone_detail,
    mileStone_delete,
    mileStone_edit,
# milestory
    mileStory_create,
    mileStory_delete,
    mileStory_detail,
    mileStory_list,
    mileStory_edit,
    add_user,
    my_mileStory_list
	)

urlpatterns = [
    url(r'^register', add_user, name='register'),
	url(r'^$', mileStory_list, name='storylist'),
    url(r'^my/', my_mileStory_list, name='mystorylist'),
    url(r'^create/$', mileStory_create, name='storycreate'),
    url(r'^(?P<story_id>[0-9]+)/$', mileStory_detail, name='storydetail'),
    url(r'^(?P<story_id>[0-9]+)/edit/', mileStory_edit, name='storyedit'),
    url(r'^(?P<story_id>[0-9]+)/delete/', mileStory_delete, name='storydelete'),
    url(r'^(?P<story_id>[0-9]+)/createstone/', mileStone_create, name='stonecreate'),
    url(r'^(?P<story_id>[0-9]+)/stone/(?P<milestone_id>[0-9]+)/$', mileStone_detail, name='stonedetail'),
    url(r'^(?P<story_id>[0-9]+)/stone/(?P<milestone_id>[0-9]+)/edit/', mileStone_edit, name='stoneedit'),
    url(r'^(?P<story_id>[0-9]+)/stone/(?P<milestone_id>[0-9]+)/delete/', mileStone_delete, name='stonedelete'),
]
#TODO if request user == story holder user then add edit create icon
#TODO how to login user?