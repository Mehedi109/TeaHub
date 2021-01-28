from django.db import models
from mainapp.models import spotlight_body,favourite_tea
from django.contrib.auth.models import User

class ShopCart(models.Model):
	tea=models.ForeignKey(spotlight_body,on_delete=models.CASCADE,null=True)
	user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
	quantity=models.IntegerField()
	#def __str__(self):
		#return self.spotlight_body.title
	def price(self):
		return self.quantity*self.tea.price

#class ShopingCartForm(Modelform):
class cart(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	product=models.ForeignKey(spotlight_body,on_delete=models.CASCADE)
	quantity=models.IntegerField()
	status=models.BooleanField(default=False)
	added_on=models.DateTimeField(auto_now_add=True,null=True)
	update_on=models.DateTimeField(auto_now=True,null=True)

	def __str__(self):
		return self.user.username
@staticmethod
def get_products_by_id(ids):
	return spotlight_body.objects.filter(id__in=ids)
class getProducts(models.Model):
	name=models.CharField(max_length=100)
class sky(models.Model):
	name=models.CharField(max_length=100)
class booking(models.Model):
	name=models.CharField(max_length=100)
class reserve(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	name=models.CharField(max_length=100)
	address=models.CharField(max_length=100)
	email_address=models.EmailField(max_length=100)
	phone=models.CharField(max_length=100)
	postal_code=models.CharField(max_length=100)
	status=models.BooleanField(default=False)
	added_on=models.DateTimeField(auto_now_add=True,null=True)
	update_on=models.DateTimeField(auto_now=True,null=True)

	def __str__(self):
		return self.name



		


	

	