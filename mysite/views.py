from django.shortcuts import render_to_response
from django.template import RequestContext

def home(request):
	return render_to_response('home.html', context_instance=RequestContext(request))

def facilities(request):
	return render_to_response('facilities.html', context_instance=RequestContext(request))

def contact(request):
	return render_to_response('contact.html', context_instance=RequestContext(request))

def location(request):
	return render_to_response('location.html', context_instance=RequestContext(request))

def members(request):
	return render_to_response('members.html', context_instance=RequestContext(request))

def classes(request):
	return render_to_response('classes.html', context_instance=RequestContext(request))
