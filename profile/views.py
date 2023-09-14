from django.shortcuts import render, redirect 
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm

from .forms import NewUserForm

def index(request):
	return render(request,'frontpage.html')

def register_request(request):
	# checks if HTTP request is POST
	if request.method == "POST":
		# instance of NewUserForm with POST data 
		form = NewUserForm(request.POST)

		if form.is_valid():
			# form data => user account
			user = form.save()
			# session for user 
			login(request, user)
			# redirects to post_all page
			return redirect("post_all")
		else:
			messages.error(request, "Unsuccessful registration. Invalid information.")

	# initializes the form	
	form = NewUserForm()
	# render 
	return render (request=request, template_name="register.html", context={"register_form":form})

def login_request(request):
	# checks if HTTP request is POST
	if request.method == "POST":
		# instance of AuthenticationForm with POST data 
		form = AuthenticationForm(request, data=request.POST)

		if form.is_valid():
			# extracting data from form 
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			# authenticates user 
			user = authenticate(username=username, password=password)

			# if sucessfully authenticated 
			if user is not None:
				# login user
				login(request, user)
				return redirect("post_all")
			else:
				messages.error(request,"Invalid username or password.")

		else:
			messages.error(request,"Invalid username or password.")

	# initializes the form	
	form = AuthenticationForm()
	# render 
	return render(request=request, template_name="login.html", context={"login_form":form})