from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages
from gallery.models import Gallery
from django.core.paginator import *
from forms import GalleryForm
from JHTS.settings import POSTS_PER_PAGE
from django.contrib.auth.decorators import login_required

def index(request):
    images = Gallery.objects.all()
    paginator = Paginator(images, POSTS_PER_PAGE)
    page = request.GET.get('page')
    try:
        images = paginator.page(page)
    except PageNotAnInteger:
        images = paginator.page(1)
    except EmptyPage:
        images = paginator.page(1)
    return render(request, 'gallery/index.html', {'images': images})

def detail(request, gallery_id):
	image = get_object_or_404(Gallery, pk=gallery_id)
	return render(request, 'gallery/detail.html', {'image': image})

@login_required
def upload(request, template_name="gallery/form.html"):   
    form = GalleryForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, template_name, {'form':form})

@login_required
def delete(request, gallery_id):
	image = get_object_or_404(Gallery, pk=gallery_id)
	image.delete()
	messages.success(request, 'Image has been deleted')
	return redirect('index')