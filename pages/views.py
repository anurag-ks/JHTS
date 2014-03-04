from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.paginator import *
from blog.models import Blog
from blog.forms import BlogForm


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

    return render(request, 'pages/index.html', {
        'posts': posts
        })


# def gallery(request):
    pass


#def controller(request):
#    return render(request, 'pages/skeleton.html', {})


# def detail(request, blog_id):
#     post = get_object_or_404(Blog, pk=blog_id)
#     return render(request, 'main/detail.html', {'post': post})


# def delete(request, blog_id):
#     post = get_object_or_404(Blog, pk=blog_id)
#     post.delete()
#     messages.success(request, 'Post has been deleted')
#     return redirect('index')


# def update(request, blog_id, template_name='main/form.html'):
#     post = get_object_or_404(Blog, pk=blog_id)
#     form = BlogForm(request.POST or None, instance=post)
#     if form.is_valid():
#         form.save()
#         messages.success(request, 'Post has been updated')
#         return redirect('index')
#     return render(request, template_name, {'form': form})


# def create(request, template_name='main/form.html'):
#     form = BlogForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         messages.success(request, 'Post has been created')
#         return redirect('index')
#     return render(request, template_name, {'form': form})
