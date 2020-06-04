from django.contrib import admin

from .models import Kandydat, Kand_Glos, Glosowanie, User_Glosowanie, CustomUser

# Register your models here.

admin.site.register(Kandydat)
admin.site.register(Kand_Glos)
admin.site.register(Glosowanie)
admin.site.register(User_Glosowanie)
admin.site.register(CustomUser)