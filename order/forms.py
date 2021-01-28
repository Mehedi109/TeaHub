from django import forms
from . models import reserve

class reserveForm(forms.ModelForm):
	class Meta:
		model=reserve
		fields=[
			'name',
			'email_address',
			'phone',
			'address',
			'postal_code'
		]