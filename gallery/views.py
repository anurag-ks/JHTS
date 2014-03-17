from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from gallery.models import GalleryPhoto
from django.core.paginator import *
from forms import GalleryForm
from JHTS.settings import POSTS_PER_PAGE
from django.contrib.auth.decorators import login_required


def index(request):
    """
        Index view for the Gallery.
    """
    images = GalleryPhoto.objects.all()
    paginator = Paginator(images, POSTS_PER_PAGE)
    page = request.GET.get('page')
    try:
        images = paginator.page(page)
    except PageNotAnInteger:
        images = paginator.page(1)
    except EmptyPage:
        images = paginator.page(1)
    return render(request, 'gallery/index.html', {'gallery_images': images})


def detail(request, gallery_id):
    """
        Detail view for a particular gallery photo.
    """
    image = get_object_or_404(GalleryPhoto, pk=gallery_id)
    return render(request, 'gallery/detail.html', {'image': image})


@login_required
def upload(request, template_name="gallery/form.html"):
    """
        View to upload a new photo.
        Just for the SuperUser.
    """
    if request.user.is_superuser:
        form = GalleryForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request, "image has been uploaded")
            return redirect('gallery.views.index')

        return render(request, template_name, {'form': form})
    else:
        messages.success(request, 'You are not authorized')
        return redirect('index')


@login_required
def delete(request, gallery_id):
    """
        View to delete a particular photo.
        Just for the SuperUser.
    """
    if request.user.is_superuser:
        image = get_object_or_404(GalleryPhoto, pk=gallery_id)
        image.delete()
        messages.success(request, 'Image has been deleted')
        return redirect('gallery.views.index')
    else:
        messages.success(request, 'You are not authorized')
        return redirect('index')
