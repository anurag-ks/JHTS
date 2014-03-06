from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.paginator import *
from django.contrib.auth.decorators import login_required
from blog.models import Blog
from pages.models import Page
from pages.forms import PageForm


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


def controller(request, url):
    page = get_object_or_404(Page, url=url)
    return render(request, 'pages/skeleton.html', {'page': page})


@login_required
def all(request):
    page_list = Page.objects.all()
    paginator = Paginator(page_list, 5)
    page_number = request.GET.get('page')
    try:
        pages = paginator.page(page_number)
    except PageNotAnInteger:
        pages = paginator.page(1)
    except EmptyPage:
        pages = paginator.page(1)

    return render(request, 'pages/all.html', {
        'pages': pages
        })


@login_required
def create(request):
    form = PageForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Page has been created')
        return redirect('index')
    return render(request, 'pages/form.html', {
        'form': form,
        'update': False
        })


@login_required
def delete(request, url):
    page = get_object_or_404(Page, url=url)
    page.delete()
    messages.success(request, 'Page has been deleted')
    return redirect('index')


@login_required
def update(request, url):
    page = get_object_or_404(Page, url=url)
    form = PageForm(request.POST or None, instance=page)
    if form.is_valid():
        form.save()
        messages.success(request, 'Page has been updated')
        return redirect('pages.controller', url=page.url)
    return render(request, 'pages/form.html', {
        'form': form,
        'update': True
        })
