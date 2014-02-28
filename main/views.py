from django.shortcuts import render, get_object_or_404, redirect
from django.forms import ModelForm
from main.models import Blog

class BlogForm(ModelForm):
    class Meta:
        model = Blog

def index(request):
	posts = Blog.objects.all().order_by('-pub_date')[:5]
	return render(request, 'main/index.html', {'posts': posts})

def detail(request, blog_id):
    post = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'main/detail.html', {'post': post})

def delete(request, blog_id):
	post = get_object_or_404(Blog, pk=blog_id)
	post.delete()
	return redirect('index')

def update(request, blog_id, template_name = 'main/form.html'):
	post = get_object_or_404(Blog, pk=blog_id)
	form = BlogForm(request.POST or None, instance=post)
	if form.is_valid():
		form.save()
		return redirect('index')
	return render(request, template_name, {'form':form})

def create(request, template_name = 'main/form.html'):
	form = BlogForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('index')
	return render(request, template_name,{'form':form})
