from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.http import HttpResponse
from django.conf import settings

def login(request):
	
	if request.method=='POST':
		username=request.POST['username']
		password=request.POST['password']

		user=auth.authenticate(username=username,password=password)

		if user is not None:
			auth.login(request,user)
			return redirect('/')
		else:
			messages.error(request,'Username or Password is incorrect')
			return redirect('login')
	else:
		return render(request,'accounts/login.html')

def register(request):
	if request.method=='POST':
		username=request.POST['username']	
		email=request.POST['email']	
		password1=request.POST['password1']	
		password2=request.POST['password2']	
		if password1==password2:
			if User.objects.filter(username=username).exists():
				messages.error(request,'Username Already Taken')
				return redirect('register')
			elif User.objects.filter(email=email).exists():
				messages.error(request,'Email Already Taken')
				return redirect('register')
			elif len (password1)<8:
				messages.error(request,'Password is too short')
				return redirect('register')
			else:
				user=User.objects.create_user(username=username,password=password1,email=email)
				#user.is_active=False
				user.save();
				messages.success(request,'Registration Successful')
				#return HttpResponse()
				return redirect('login')
		else:
			messages.error(request,'password not matching')
			return redirect('register')
				#return redirect('/')

	else:
	    return render(request,'accounts/register.html')

def logout(request):
	auth.logout(request)
	return redirect('/')
