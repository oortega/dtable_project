# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from table.models import Autor, Libro, FacturaCached
# Register your models here.


class AutorAdmin(admin.ModelAdmin):
	list_display= ('nombre', 'apellidos', 'email')
	search_fields=('nombre', 'apellidos')

class LibroAdmin(admin.ModelAdmin):
	list_display= ('titulo', 'fecha_publicacion')
	list_filter=('fecha_publicacion',)
	date_hierarchy ='fecha_publicacion'
	ordering = ('fecha_publicacion',)
	filter_horizontal = ('autor',)

class FacturaCachedAdmin(admin.ModelAdmin):
	list_display= ('key',)
	list_filter=('key',)


admin.site.register(Autor, AutorAdmin)
admin.site.register(Libro, LibroAdmin)
admin.site.register(FacturaCached, FacturaCachedAdmin)