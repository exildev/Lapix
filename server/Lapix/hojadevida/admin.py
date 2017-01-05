#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import admin
from exileui.admin import exileui
import forms
import models
# Register your models here.


class ProfesorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'identificacion',
                    'fecha', 'telefono', 'direccion', 'status')
    search_fields = ('first_name', 'last_name', 'identificacion')
    list_filter = ('sexo', 'status')
    form = forms.ProfesorForm

    def get_form(self, request, obj=None, *args, **kwargs):
        if obj:
            kwargs['form'] = forms.EditProfesor
        # end if
        return super(ProfesorAdmin, self).get_form(request, obj, *args, **kwargs)
    # end def
# end class


class EstudianteAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'identificacion', 'fecha', 'telefono',
                    'direccion', 'grado', 'codigo_Estudiante', 'colegio_Anterior', 'status')
    search_fields = ('first_name', 'last_name', 'identificacion')
    list_filter = ('sexo', 'grado', 'status')
# end class


class AcudienteAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'identificacion',
                    'fecha', 'telefono', 'direccion', 'status')
    filter_horizontal = ('estudiantes',)
    search_fields = ('first_name', 'last_name', 'identificacion')
    list_filter = ('sexo', 'status')
# end class

exileui.register(models.Profesor, ProfesorAdmin)
exileui.register(models.Estudiante, EstudianteAdmin)
exileui.register(models.Acudiente, AcudienteAdmin)
exileui.register(models.AsiganacionSede)
