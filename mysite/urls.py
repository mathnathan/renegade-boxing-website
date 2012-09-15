from django.conf.urls import patterns, include, url
from django.contrib import admin
import payments.urls as payment_urls
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'mysite.views.home', name='home'),
    url(r'^home/$', 'mysite.views.home', name='home'),
	url(r'^members/', 'mysite.views.members', name='members'),
	url(r'^facilities/', 'mysite.views.facilities', name='facilities'),
	url(r'^contact/', 'mysite.views.contact', name='contact'),
	url(r'^location/', 'mysite.views.location', name='location'),
	url(r'^classes/', 'mysite.views.classes', name='classes'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^payments/', include(payment_urls)),
	url(r'^grappelli/', include('grappelli.urls')),
)
