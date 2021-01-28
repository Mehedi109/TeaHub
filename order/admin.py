from django.contrib import admin

from . models import ShopCart
admin.site.register(ShopCart)

class ShopCartAdmin(admin.ModelAdmin):
	list_display=['tea','quantity','price','amount']
	list_filter=['user']

from . models import cart 
admin.site.register(cart)
from . models import getProducts,sky,booking,reserve
admin.site.register(getProducts)
admin.site.register(sky)
admin.site.register(booking)
admin.site.register(reserve)
