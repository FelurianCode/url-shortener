from django.shortcuts import render
from rest_framework import generics
from django.http import HttpResponse, HttpResponseRedirect
from .models import Url
from .serializers import UrlSerializer
from .forms import UrlForm
import uuid 

def index(request):
	#if form submitt ed
	if request.method == 'POST':
		form = UrlForm(request.POST)
		# check whether it's valid:
		if form.is_valid():
			url = Url() #urlobject
			url.original_url = form.cleaned_data['url']
			url.url_code = create_code()

			url.save()
			url_result = request.build_absolute_uri() + 'url/' + url.url_code
			return render(request, 'urls/index.html', {'form': form, 'new_url': url_result})

	# if other we'll create a blank form
	else:
		form = UrlForm()
		return render(request, 'urls/index.html', {'form': form})

def redirect_url(request, code):
	url_result = Url.objects.get(url_code=code) #urlobject
	serializer_class = UrlSerializer
	return HttpResponseRedirect(url_result.original_url)	



def create_code():
	code = uuid.uuid4().hex[:8].upper()
	return code
		

