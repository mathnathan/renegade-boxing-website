from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from forms import ContactForm

def home(request):
	return render_to_response('home.html', context_instance=RequestContext(request))

def news(request):
	return render_to_response('news.html', context_instance=RequestContext(request))

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
