from django import forms
from .models import spotlight_body,favourite_tea,article,postComment

class spotlight_bodyForm(forms.ModelForm):
	class Meta:
		model=spotlight_body
		fields="__all__"
class favourite_teaForm(forms.ModelForm):
	class Meta:
		model=favourite_tea
		fields="__all__"

class articleForm(forms.ModelForm):
	class Meta:
		model=article
		fields="__all__"

class postCommentForm(forms.ModelForm):
	class Meta:
		model=postComment
		fields=[
			'name',
			'email',
			'comment',
		]