from django.shortcuts import render_to_response, get_object_or_404
from members.models import Information

def index(request):
	names = Information.objects.all()
	context = render_to_response('index.htm', {'names': names})
	return context
