from django.shortcuts import render, redirect
from .forms import BlogForm
from .models import BlogModel

# Create your views here.
def index (request):

    posts = BlogModel.objects.all()

    context={
    'heading':'List Post',
    'post':posts
    }

    return render (request, "blog/index.html",context)

def create (request):
    cont_form= BlogForm(request.POST)

    if request.method == 'POST':
        if cont_form.is_valid():
            BlogModel.objects.create( #tanpa ini, harus dibawah context
                #cara dibawah ambil ambil data yg sudah divalidasi, bukan raw lagi
                judul    = cont_form.cleaned_data.get('judul'), #context['judul'] = request.POST['judul'],
                body     = cont_form.cleaned_data.get('body'), #context['body'] = request.POST['body'],
                category = cont_form.cleaned_data.get('category'), #context['category'] = request.POST['category'],
            )

            return redirect ("/blog/")

    context={
    'heading':'Create Post',
    'contact_form':cont_form,
    }

    return render (request, "blog/create.html",context)
