from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'zebra/', include('zebra.urls', namespace="zebra", app_name='zebra') ),
)
