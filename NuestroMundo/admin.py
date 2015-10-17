from django.contrib import admin

from .models import Pais, Ciudad, Idioma_Pais, Idioma

# Register your models here.
admin.site.register(Pais)
admin.site.register(Ciudad)
admin.site.register(Idioma_Pais)
admin.site.register(Idioma)