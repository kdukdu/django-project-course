from django.urls import re_path, path

from . import views

app_name = 'blog'

urlpatterns = [
    re_path(r'^$', views.PostListView.as_view(), name='index'),
    re_path(r'^tag/(?P<tag_slug>[-\w]+)/$', views.PostListView.as_view(), name='post-list-by-tag'),
    re_path(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$', views.post_detail,
            name='post_detail'),
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),

]
