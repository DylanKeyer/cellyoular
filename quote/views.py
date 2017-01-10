from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from quote.forms import PhoneForm

# Create your views here.
def index(request):
    return HttpResponse("Quote application goes here.")


def add_phone(request):
    if request.method == 'POST':
        form = PhoneForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print(form.errors)
    else:
        form = PhoneForm()

    return render(request, 'quote/quote.html', {'form': form})