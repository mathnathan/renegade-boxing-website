from django.conf import settings
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.utils.encoding import smart_str
from forms import ContactForm
from os.path import isfile, join

def home(request):
	return render_to_response('home.html', context_instance=RequestContext(request))

def download(request, file=None):
	if file == None:
		return HttpResponseNotFound('<h1>Sorry, that file does not exist!</h1>')

	response = HttpResponse(my_data, content_type='static/base/media/'+file)
	response['Content-Disposition'] = 'attachment; filename='+file

def news(request):
	return render_to_response('news.html', context_instance=RequestContext(request))

def fcbc1(request):
	return render_to_response('fcbc1.html', context_instance=RequestContext(request))

def fcbc1_videos(request):
	return render_to_response('fcbc1_videos.html', context_instance=RequestContext(request))

def facility(request):
	return render_to_response('facility.html', context_instance=RequestContext(request))

def contact(request):
	if request.method == 'POST': # If the form has been submitted...
		form = ContactForm(request.POST) # A form bound to the POST data
		if form.is_valid(): # All validation rules pass
			# Process the data in form.cleaned_data
			# ...
			return HttpResponseRedirect('/home/') # Redirect after POST
	else:
		form = ContactForm() # An unbound form

	return render_to_response('contact.html', {'form': form}, context_instance=RequestContext(request))

def staff(request):
	return render_to_response('staff.html', context_instance=RequestContext(request))

def team(request):
	return render_to_response('team.html', context_instance=RequestContext(request))

def members(request):
	return render_to_response('members.html', context_instance=RequestContext(request))

def classes(request):
	return render_to_response('classes.html', context_instance=RequestContext(request))

def downloads(request, file_name):
	dl_item = join( settings.DOWNLOAD_DIR, file_name )
	if isfile( dl_item ):
		response = HttpResponse(mimetype='application/force-download')
		response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(file_name)
		response['X-Sendfile'] = smart_str( dl_item )
		return response
	else:
		return HttpResponseRedirect('/home/') # Redirect after POST
