from django.contrib import admin
from .models import Album,Musica, Usuario

from django.contrib.auth.admin import UserAdmin
# Register your models here.

campos = list(UserAdmin.fieldsets)

campos.append(
    ("Minha Play List", {"fields": ("play_list", )})

)

UserAdmin.fieldsets = tuple(campos)

admin.site.register(Album)
admin.site.register(Musica)
admin.site.register(Usuario, UserAdmin)