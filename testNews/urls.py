from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.news, name='news'),
    url(r'^text/(?P<pk>\d+)/$', views.news_text, name='news_text'),
    url(r'^list/$', views.news_list, name='news_list'),
    # url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    # url(r'^post/new/$', views.post_new, name='post_new'),
    # url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
]
