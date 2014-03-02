from django.conf.urls import patterns, include, url
from main import views
urlpatterns = patterns('',
	url(r'^$', views.index, name = 'index'),
	url(r"^(?P<blog_id>\d+)/$", views.detail, name='detail'),
	url(r"^(?P<blog_id>\d+)/delete/$", views.delete, name='delete'),
	url(r"^(?P<blog_id>\d+)/update/$", views.update, name='update'),
	url(r"^new/$", views.create, name='create'),
	url(r"^about/$", views.about, name='about'),
	url(r"^curriculum/$", views.curriculum, name='curriculum'),
	url(r"^services/$", views.services, name='services'),
	url(r"^contact/$", views.contact, name='contact'),
	url(r"^gallery/$", views.gallery, name='gallery'),
	)