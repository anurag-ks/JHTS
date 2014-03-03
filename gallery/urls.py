from django.conf.urls import patterns, include, url
from gallery import views

urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
    url(r"^(?P<gallery_id>\d+)/$", views.detail, name='detail'),
    url(r"^(?P<gallery_id>\d+)/delete/$", views.delete, name='delete'),
    url(r"^new/$", views.create, name='create'),
    )