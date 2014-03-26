from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from blog.models import Blog
from django.core.paginator import *
from forms import BlogForm
from JHTS.settings import POSTS_PER_PAGE
from django.contrib.auth.decorators import login_required


def index(request):
    """
        Index view for the blog.
    """
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


def tag_filter(request, tag):
    '''
        This view requires a nice form.
        At this moment it can be tested by manually typing in the url.
    '''
    tag.lower()
    results = Blog.objects.filter(tags__name__in=[tag])
    return render(request, 'main/filter.html', {'results': results})


def detail(request, blog_id):
    """
        View for a single blog post.
    """
    post = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'main/detail.html', {'post': post})


@login_required
def delete(request, blog_id):
    """
        View to delete a particular blog post.
        Just for the SuperUser.
    """
    if request.user.is_superuser:
        post = get_object_or_404(Blog, pk=blog_id)
        post.delete()
        messages.success(request, 'Post has been deleted')
        return redirect('index')
    else:
        messages.success(request, 'You are not authorized')
        return redirect('index')


@login_required
def update(request, blog_id, template_name='main/form.html'):
    """
        View to update a particular blog post.
        Just for the SuperUser.
    """
    if request.user.is_superuser:
        post = get_object_or_404(Blog, pk=blog_id)
        form = BlogForm(request.POST or None, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post has been updated')
            return redirect('index')
        return render(request, template_name, {'form': form})
    else:
        messages.success(request, 'You are not authorized')
        return redirect('index')


@login_required
def create(request, template_name='main/form.html'):
    """
        View to create a new blog post.
        Just for the SuperUser.
    """
    if request.user.is_superuser:
        form = BlogForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post has been created')
            return redirect('index')
        return render(request, template_name, {'form': form})
    else:
        messages.success(request, 'You are not authorized')
        return redirect('index')
