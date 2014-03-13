from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django import forms

class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit = False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

def signup(request, template_name="registration/signup.html"):
    form = UserCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request,
                         'User Account Created. Please proceed to login.')
        return redirect('/login/')
    return render(request, template_name, {'form': form})


def error404(request):
    render(request, "404.html")
