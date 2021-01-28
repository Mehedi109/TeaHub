from django.shortcuts import render,redirect,get_object_or_404,HttpResponse
from django.conf import settings
#from django.template.Library.filter()
from django.contrib.auth.models import User,auth
from django.http import JsonResponse
from . models import cart,reserve
from . forms import reserveForm
from mainapp.models import spotlight_body,favourite_tea
def add_to_cart(request):
	context={}
	#usr=get_object_or_404(User,id=request.user.id)
	#items=cart.objects.filter(user=usr.id)
	items=cart.objects.filter(user__id=request.user.id,status=False)
	context["items"]=items
	if request.user.is_authenticated:
		if request.method=="POST":
			pid=request.POST["pid"]
			qty=request.POST["qty"]
			#total=qty*product.price
			is_exist=cart.objects.filter(product__id=pid,user__id=request.user.id,status=False)
			if len(is_exist)>0:
				context["msz"]="Item already  Exists in Your Cart"
				context["cls"]="alert alert-warning"
			else:
				product=get_object_or_404(spotlight_body,id=pid)
				#product=get_object_or_404(favourite_tea,id=pid)  #### NEW
				usr=get_object_or_404(User,id=request.user.id)
				c=cart(user=usr,product=product,quantity=qty)  #### NEW
				c.save()
				context["msz"]="Item added in Your Cart"
				context["cls"]="alert alert-success"
	else:
		context["status"] = "Please login to View Your Cart"
	return render(request,'order/cart.html',context)

def get_cart_data(request):
	items=cart.objects.filter(user__id=request.user.id,status=False)
	sale,total,quantity=0,0,0
	for post in items:
		sale=int(post.product.price)
		total+=int(post.product.price)*post.quantity
		quantity+=int(post.quantity)

	res={
		"total":total,"price":sale,"quantity":quantity,
	}
	return JsonResponse(res)

def price_total(request):
	items=cart.objects.filter(user__id=request.user.id,status=False)
	if request.method=="POST":
		qty=request.POST["qty"]
		sum=product.price*qty
	return render(request,'order/cart.html')
	#return product.price*cart_quantity()
def change_quan(request):
	if "quantity" in request.GET:
		cid=request.GET["cid"]
		qty=request.GET["quantity"]
		cart_obj=get_object_or_404(cart,id=cid)
		cart_obj.quantity=qty
		cart_obj.save()
		return HttpResponse(cart_obj.quantity)
	if "delete_cart" in request.GET:
		id=request.GET["delete_cart"]
		cart_obj=get_object_or_404(cart,id=id)
		cart_obj.delete()
		return HttpResponse(1)

def order(request):
	if request.method == "POST":
		form=reserveForm(request.POST)
		if form.is_valid():
			try:
				if request.user.is_authenticated:
					the_form=form.save(commit=False)
					the_form.user=request.user
					the_form.save()
					messages.success(request,'Your Booking is done Successfully')
					#messages.warning(request,'Sorry there is no ambulance available on that time.Your desired ambulance is available on 6 p.m to 10 p.m')
					return redirect("/order")

				else:
					messages.info(request,'Please login your account')
					return redirect('accounts/login')
					if user is not None:
						auth.login(request,user)
						return redirect('/order')
			except:
				pass
	else:
		form=reserveForm()
		return render(request,"order/order.html",{"form":form})
	return HttpResponse('order confirmed')

def customer(request):
	post=reserve.objects.all()
	context={
		"post":post
	}
	return render(request,"admin/customer.html",context)
def customer_delete(request,id):
	post=get_object_or_404(reserve,id=id)
	post.delete()
	return redirect('customer')
def customer_details(request,id):
	usr=User.objects.all()
	post=reserve.objects.filter(user=id)
	#user=User.objects.get(username=username)
	#user=User.objects.all
	items=cart.objects.filter(status=False,user=id)
	context={
		"post":post,
		"items":items,
	}
	return render(request,"order/customer_details.html",context)
def customer_cart_data(request):
	items=cart.objects.filter(user=request.user.id,status=False)
	sale,total,quantity=0,0,0
	for post in items:
		sale=int(post.product.price)
		total+=int(post.product.price)*post.quantity
		quantity+=int(post.quantity)

	res={
		"total":total,"price":sale,"quantity":quantity,
	}
	return JsonResponse(res)