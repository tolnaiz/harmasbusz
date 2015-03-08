from django.conf.urls import patterns, include, url
from django.contrib import admin
import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'harmasbusz.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'harmasbusz.views.index', name='index'),
    url(r'^update$', 'harmasbusz.views.update', name='index')
)
