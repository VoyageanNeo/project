from django.conf.urls import url

from .views import (
    mileStone_create,
    mileStone_detail,
    mileStone_list,
    mileStone_delete
	)
urlpatterns = [
	url(r'^$', mileStone_list, name='list'),
    url(r'^create/$', mileStone_create, name='create'),
    url(r'^(?P<slug>[\w-]+)/$', mileStone_detail, name='detail'),
    #TODO make view to edit milestoen
    url(r'^(?P<slug>[\w-]+)/delete/$', mileStone_delete, name='delete'),
]
