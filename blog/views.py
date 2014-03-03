from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from blog.models import Blog
from django.core.paginator import *
from forms import BlogForm
from JHTS.settings import POSTS_PER_PAGE
from django.contrib.auth.decorators import login_required


def index(request):
    post_list = Blog.objects.all().order_by('-pub_date')
    paginator = Paginator(post_list, POSTS_PER_PAGE)
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


@login_required
def delete(request, blog_id):
    post = get_object_or_404(Blog, pk=blog_id)
    post.delete()
    messages.success(request, 'Post has been deleted')
    return redirect('index')


@login_required
def update(request, blog_id, template_name='main/form.html'):
    post = get_object_or_404(Blog, pk=blog_id)
    form = BlogForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        messages.success(request, 'Post has been updated')
        return redirect('index')
    return render(request, template_name, {'form': form})


@login_required
def create(request, template_name='main/form.html'):
    form = BlogForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Post has been created')
        return redirect('index')
    return render(request, template_name, {'form': form})
