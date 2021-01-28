from django.shortcuts import render,redirect,get_object_or_404,HttpResponse
from . models import slider,tea_info,spotlight_body,favourite_tea,article,postComment,Usermessage
from . forms import spotlight_bodyForm,favourite_teaForm,articleForm,postCommentForm

def index(request):
	post1=slider.objects.all()
	post2=tea_info.objects.all()
	post3=spotlight_body.objects.all()
	post4=favourite_tea.objects.all()
	context={
		'post1':post1,
		'post2':post2,
		'post3':post3,
		'post4':post4,
	}
	return render(request,"index.html",context)
def maintea(request):
	#if request.method == "POST":			
	form=spotlight_bodyForm(request.POST or None,request.FILES or None)			
	if form.is_valid():				
		instance=form.save(commit=False)				
		instance.save();				
		return redirect('admin_mainTea')	
	return render (request,"maintea.html",{"form":form})
def maintea_update(request,id):
	#if request.user.is_authenticated:
	if request.user.is_staff or request.user.is_superuser:
		post=get_object_or_404(spotlight_body,id=id)
		#post=article.objects.get(id=id)
		form=spotlight_bodyForm(request.POST or None,instance=post)
		if form.is_valid():
		   instance=form.save(commit=False)
		   instance.save()
		   #messages.success(request,'Updated Successfully')
		   return redirect('admin_mainTea')
		return render(request,"maintea.html",{"form":form})
	return HttpResponse()
def maintea_delete(request,id):
	post=get_object_or_404(spotlight_body,id=id)
	post.delete()
	return redirect('admin_mainTea')
def favouriteTea(request):
	#if request.method == "POST":			
	form=favourite_teaForm(request.POST or None,request.FILES or None)			
	if form.is_valid():				
		instance=form.save(commit=False)				
		instance.save();				
		return redirect('/')	
	return render (request,"favourite_tea.html",{"form":form})
def favouriteTea_update(request,id):
	post=get_object_or_404(favourite_tea,id=id)			
	form=favourite_teaForm(request.POST or None,instance=post)			
	if form.is_valid():				
		instance=form.save(commit=False)				
		instance.save();				
		return redirect('admin_favouriteTea')	
	return render (request,"favourite_tea.html",{"form":form})
def favouriteTea_delete(request,id):
	post=get_object_or_404(favourite_tea,id=id)
	post.delete()
	return redirect('admin_favouriteTea')
def contact(request):
	if request.method == 'POST':
			post_message=Usermessage()
			name=request.POST['name']
			email=request.POST['email']
			subject=request.POST['subject']
			message=request.POST['message']
			post_message.name=name
			post_message.email=email
			post_message.subject=subject
			post_message.message=message
			post_message.save()
			return HttpResponse('<h1>Thanks for messaging us</h1>')
	return render(request,'contact.html')
def admin(request):
	return render(request,"admin/admin.html")
def admin_mainTea(request):
	post=spotlight_body.objects.all()
	return render(request,"admin/admin_mainTea.html",{"post":post})
def admin_favouriteTea(request):
	post=favourite_tea.objects.all()
	return render(request,"admin/admin_favouriteTea.html",{"post":post})
def admin_blog(request):
	post=article.objects.all().order_by('id')
	return render(request,'admin/admin_blog.html',{"post":post})
def blog(request):
	post=article.objects.all().order_by('id')
	context={
		"post":post,
	}
	return render(request,"blog.html",context)
	#return HttpResponse()
def single_blog(request,id):
	post=get_object_or_404(article,id=id)
	getComment=postComment.objects.filter(post=id)
	if request.method=="POST":
		form=postCommentForm(request.POST or None)
		if form.is_valid():
			instance=form.save(commit=False)
			instance.post=post
			parent_id = request.POST.get('comment_id') #reply-section
			comment_qs=None
			if parent_id:
				comment_qs = postComment.objects.get(id=parent_id)
			instance.save()
		return redirect('single_blog',id)
	else:	
		form=postCommentForm()
		context={
			"post":post,
			"form":form,
			"comment":getComment,
		}
	return render(request,"single_blog.html",context)

def post(request):
	if request.user.is_authenticated:
		form=articleForm(request.POST or None)
		if form.is_valid():
			instance=form.save(commit=False)
			instance.save();
			return redirect('/blog')
	return render (request,"create_blog.html",{"form":form})

def blog_update(request,id):
	#if request.user.is_authenticated:
	if request.user.is_staff or request.user.is_superuser:
		post=get_object_or_404(article,id=id)
		#post=article.objects.get(id=id)
		form=articleForm(request.POST or None,instance=post)
		if form.is_valid():
		   instance=form.save(commit=False)
		   instance.save()
		   #messages.success(request,'Updated Successfully')
		   return redirect('/admin_blog')
		return render(request,"create_blog.html",{"form":form})
	return HttpResponse()

def blog_delete(request,id):
	#if request.user.is_authenticated:
	if request.user.is_staff or request.user.is_superuser:
		post=get_object_or_404(article,id=id)
		post.delete()
		return redirect('/admin_blog')
