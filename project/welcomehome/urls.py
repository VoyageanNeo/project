from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from . import views

app_name = 'welcomehome'
urlpatterns = [
    url(r'^$', views.person_list, name='list'),
    url(r'^enroll/$', views.person_enroll, name='enrol'),
    url(r'^(?P<id>\d+)/$', views.person_detail, name='detail'),
    url(r'^(?P<id>\d+)/delete/$', views.person_delete, name='delete'),
    url(r'^(?P<id>\d+)/edit/$', views.person_update, name='update'),
]
