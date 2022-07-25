from django.shortcuts import render
from .forms import HomeForm

def index (request):
    context={
    'heading':'List Post'
    }
    return render (request, "index.html",context)

def create (request):
    cont_form= HomeForm()
    if request.method == 'POST':
        print (request, 'POST')
    context={
    'heading':'Create Post',
    'contact_form':cont_form,
    }
    return render (request, "create.html",context)
