from django.urls import re_path
from . import views


app_name = 'blog'

urlpatterns = [
    re_path(r'^$', views.PostListView.as_view(), name='index'),
    re_path(r'^tag/(?P<tag_slug>[-\w]+)/$', views.PostListView.as_view(), name='post-list-by-tag'),
    re_path(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$', views.post_detail,
            name='post_detail'),
]
