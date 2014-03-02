from django.shortcuts import render, get_object_or_404, redirect
from django.forms import ModelForm
from django.contrib import messages
from main.models import Blog
from django import forms
from ckeditor.widgets import CKEditorWidget
from django.core.paginator import *

class BlogForm(ModelForm):
	content = forms.CharField(widget=CKEditorWidget())
	class Meta:
		model = Blog
def index(request):
	post_list = Blog.objects.all().order_by('-pub_date')
	paginator = Paginator(post_list, 5)
	page = request.GET.get('page')
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(1)
	return render(request, 'main/index.html', {'posts': posts})

def detail(request, blog_id):
    post = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'main/detail.html', {'post': post})

def delete(request, blog_id):
	post = get_object_or_404(Blog, pk=blog_id)
	post.delete()
	messages.success(request, 'Post has been deleted')
	return redirect('index')

def update(request, blog_id, template_name = 'main/form.html'):
	post = get_object_or_404(Blog, pk=blog_id)
	form = BlogForm(request.POST or None, instance=post)
	if form.is_valid():
		form.save()
		messages.success(request, 'Post has been updated')
		return redirect('index')
	return render(request, template_name, {'form':form})

def create(request, template_name = 'main/form.html'):
	form = BlogForm(request.POST or None)
	if form.is_valid():
		form.save()
		messages.success(request, 'Post has been created')
		return redirect('index')
	return render(request, template_name, {'form':form})

def about(request):
	template_name = 'main/about.html'
	return render(request, template_name)

def contact(request):
	template_name = 'main/contact.html'
	return render(request, template_name)
def services(request):
	template_name = 'main/services.html'
	return render(request, template_name)
def gallery(request):
	template_name = 'main/gallery.html'
	return render(request, template_name)
def curriculum(request):
	template_name = 'main/curriculum.html'
	return render(request, template_name)