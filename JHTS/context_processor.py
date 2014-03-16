from pages.models import Page

def list_pages(request):
	pages = Page.objects.all()
	return {"pages" : pages}