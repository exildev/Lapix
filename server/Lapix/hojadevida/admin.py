#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import admin
from exileui.admin import exileui
import forms
import models
# Register your models here.


class AsignacionSedeStack(admin.StackedInline):
    model = models.AsiganacionSede
    filter_horizontal = ['sede',]
    extra = 0
# end class


class ProfesorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'identificacion',
                    'fecha', 'telefono', 'direccion', 'status', 'eliminado')
    search_fields = ('first_name', 'last_name', 'identificacion')
    list_filter = ('sexo', 'status')
    form = forms.ProfesorForm
    inlines = [AsignacionSedeStack]

    def get_form(self, request, obj=None, *args, **kwargs):
        if obj:
            kwargs['form'] = forms.EditProfesor
        # end if
        return super(ProfesorAdmin, self).get_form(request, obj, *args, **kwargs)
    # end def
# end class


class EstudianteAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'identificacion', 'fecha', 'telefono',
                    'direccion', 'grado', 'codigo_Estudiante', 'colegio_Anterior', 'status', 'eliminado')
    search_fields = ('first_name', 'last_name', 'identificacion')
    list_filter = ('sexo', 'grado', 'status')
    form = forms.EstudianteForm

    def get_form(self, request, obj=None, *args, **kwargs):
        if obj:
            kwargs['form'] = forms.EdirEstudiante
        # end if
        return super(EstudianteAdmin, self).get_form(request, obj, *args, **kwargs)
    # end def
# end class


class AcudienteAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'identificacion',
                    'fecha', 'telefono', 'direccion', 'status', 'eliminado')
    filter_horizontal = ('estudiantes',)
    search_fields = ('first_name', 'last_name', 'identificacion')
    list_filter = ('sexo', 'status')
    form = forms.AcudienteForm

    def get_form(self, request, obj=None, *args, **kwargs):
        if obj:
            kwargs['form'] = forms.EditAcudiente
        # end if
        return super(AcudienteAdmin, self).get_form(request, obj, *args, **kwargs)
    # end def
# end class

exileui.register(models.Profesor, ProfesorAdmin)
exileui.register(models.Estudiante, EstudianteAdmin)
exileui.register(models.Acudiente, AcudienteAdmin)
exileui.register(models.AsiganacionSede)
exileui.register(models.GradoEntrante)
