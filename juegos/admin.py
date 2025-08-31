from django.contrib import admin

from django.contrib import admin
from .models import Categoria, Juego, Nominacion

admin.site.register(Categoria)
admin.site.register(Juego)
admin.site.register(Nominacion)