from django.contrib.auth.forms import UserCreationForm 
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User

def signup(request, template_name="registration/signup.html"):
	if request.method =='POST':
		form = UserCreationForm(request.POST or None)
		if form.is_valid():
			form.save()
			messages.success(request, 'User has been created, Now go to login !!')
	        return redirect('/login/')
		
	else :
		form = UserCreationForm() # unbound form
	return render(request, template_name, {'form':form})

# only works in production (DEBUG=False)
def error404(request):
	render(request, "404.html")
