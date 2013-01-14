from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'mysite.views.home', name='home'),
    url(r'^home/$', 'mysite.views.home', name='home'),
	url(r'^members/$', 'mysite.views.members', name='members'),
	url(r'^facility/$', 'mysite.views.facility', name='facility'),
	url(r'^news/$', 'mysite.views.news', name='news'),
	url(r'^news/fcbc1/$', 'mysite.views.fcbc1', name='fcbc1'),
	url(r'^news/fcbc1/videos/$', 'mysite.views.fcbc1_videos', name='fcbc1_videos'),
	url(r'^team/$', 'mysite.views.team', name='team'),
	url(r'^contact/$', 'mysite.views.contact', name='contact'),
	url(r'^staff/$', 'mysite.views.staff', name='staff'),
	url(r'^classes/$', 'mysite.views.classes', name='classes'),
	url(r'^downloads/(?P<file_name>.*)/$', 'mysite.views.downloads', name='downloads'),
    url(r'^admin/doc/$', include('django.contrib.admindocs.urls')),
    url(r'^admin/$', include(admin.site.urls)),
	url(r'^grappelli/$', include('grappelli.urls')),
)
