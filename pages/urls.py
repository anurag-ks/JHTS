from django.conf.urls import patterns, include, url
from pages import views

urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
    url(r'^pages/new', views.create, name='create'),
    url(r'^pages/$', views.all, name='all'),
    url(r"^(?P<url>\w+)/delete/$", views.delete, name='delete'),
    url(r"^(?P<url>\w+)/update/$", views.update, name='update'),
    url(r'^(?P<url>\w+)', views.controller, name='pages'),
    )
