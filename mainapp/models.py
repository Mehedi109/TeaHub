from django.db import models

class slider(models.Model):
	image=models.FileField()
	title=models.CharField(max_length=100)
	subtitle=models.CharField(max_length=100)
class tea_info(models.Model):
	title=models.CharField(max_length=100)
	desc=models.TextField()
class spotlight_body(models.Model):
	image=models.FileField()
	title=models.CharField(max_length=100)
	price=models.IntegerField()

	def __str__(self):
		return self.title
class favourite_tea(models.Model):
	image=models.FileField()
	title=models.CharField(max_length=100)
	desc=models.TextField()
	price=models.IntegerField()

	def __str__(self):
		return self.title

class better(models.Model):
	image=models.FileField()
	title=models.CharField(max_length=100)
	price=models.IntegerField()
class eating(models.Model):
	name=models.CharField(max_length=100)

class article(models.Model):
	title=models.CharField(max_length=50,unique=True)
	posted_on=models.DateTimeField(auto_now=False,auto_now_add=True)
	updated_on=models.DateTimeField(auto_now=True,auto_now_add=False)
	body=models.TextField()
	Category=models.CharField(max_length=100)

	def __str__(self):
		return self.title

class postComment(models.Model):
	post=models.ForeignKey(article,on_delete=models.CASCADE)
	name=models.CharField(max_length=100)
	email=models.EmailField(max_length=100)
	comment=models.TextField()
	parent=models.ForeignKey('postComment',null=True,related_name="replies",on_delete=models.CASCADE)

	def __str__(self):
		return self.post
class Usermessage(models.Model):
	name=models.CharField(max_length=50)
	email=models.EmailField(max_length=20)
	subject=models.CharField(max_length=50)
	message=models.TextField()

	def __str__(self):
		return self.name