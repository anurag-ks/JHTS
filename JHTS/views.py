from django.core.context_processors import csrf
from django.shortcuts import render_to_response, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

import sys
sys.setrecursionlimit(10000)


def login_view(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('login.html', c)


def auth_and_login(request, onsuccess='/', onfail='/login/'):
    user = authenticate(username=request.POST['username'],
                        password=request.POST['password'])
    if user is not None:
        login(request, user)
        return redirect(onsuccess)
    else:
        return redirect(onfail)


def logout_view(request):
    logout(request)
    return redirect("/")
