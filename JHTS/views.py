from django.shortcuts import render, redirect
from django.contrib import messages
from forms import UserCreateForm
from django.contrib.auth import views


# A beatiful hack :)
def login(request):
    if request.user.is_authenticated():
        messages.warning(request, 'Don\'t fuck with me.')
        return redirect('/')
    else:
        return views.login(request)


def signup(request, template_name="registration/signup.html"):
    if request.user.is_authenticated():
        messages.warning(request, 'Logout to create a new user')
        return redirect('/')
    else:
        form = UserCreateForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request,
                             'User Account Created. Please proceed to login.')
            return redirect('/login/')
        return render(request, template_name, {'form': form})


def error404(request):
    render(request, "404.html")
