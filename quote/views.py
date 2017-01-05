from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .forms import Carrier

# Create your views here.
def index(request):
    return HttpResponse("Quote application goes here.")

def get_carrier(request):
	if request.method == 'POST':
		form = Carrier(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'quote.html', {'form': form})