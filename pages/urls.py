from django.conf.urls import patterns, include, url
from pages import views

urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
    #url(r'^gallery', views.gallery, name='gallery'),
    #url(r'^(?P<url>\w+)', views.controller, name='pages'),
    )
