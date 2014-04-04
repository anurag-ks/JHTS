from django.conf.urls import patterns, url
from blog import views

urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
    url(r"^(?P<blog_id>\d+)/$", views.detail, name='detail'),
    url(r"^(?P<blog_id>\d+)/delete/$", views.delete, name='delete'),
    url(r"^(?P<blog_id>\d+)/update/$", views.update, name='update'),
    url(r"^(?P<blog_id>\d+)/comment/$", views.add_comment,
        name='add_comment'),
    url(r"^(?P<comment_id>\d+)/comment/delete/$",
        views.delete_comment, name='delete_comment'),
    url(r"^new/$", views.create, name='create'),
    url(r"^(?P<tag>\w+)/$", views.tag_filter, name='tag_filter'),
    )
