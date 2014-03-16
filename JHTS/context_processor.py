from pages.models import Page

def list_pages(request):
	pages = Page.objects.all().order_by('-title')
	return {"pages" : pages}