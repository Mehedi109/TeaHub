from django.contrib import admin

from . models import slider
from . models import tea_info
from . models import spotlight_body
from . models import favourite_tea
from . models import eating,article,Usermessage
admin.site.register(slider)
admin.site.register(tea_info)
admin.site.register(spotlight_body)
admin.site.register(favourite_tea)
admin.site.register(eating)
admin.site.register(article)
admin.site.register(Usermessage)

