from django.shortcuts import render
from django.template import RequestContext
 

from home.models import Phone
# Create your views here.

def index(request):
	
    return render(request, 'home/index1.html')
