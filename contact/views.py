from django.shortcuts import render
from .forms import ContactForm #or from . import forms (dibelakang fungsi ditambah forms.)
# Create your views here.

def index (request):
    cont_form= ContactForm()
    context={
    'heading':'Ini Heading Contact',
    'contact_form':cont_form,
    }
    return render (request, "contact/contact.html",context)
