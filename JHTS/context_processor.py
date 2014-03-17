from pages.models import Page
from gallery.models import GalleryPhoto

def list_images(request):
	images = GalleryPhoto.objects.all()
	return {"images" : images}
	
def list_pages(request):
	pages = Page.objects.all().order_by('-title')
	return {"pages" : pages}