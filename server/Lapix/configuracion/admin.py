#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import admin
from exileui.admin import exileui
import models
import forms

# Register your models here.
"""
    Para esta clase hay q aclarar lo q se validara a el editar, como el hecho q nno
    se podran realizar modificaciones una vez se de inicio a las actividaes academicas
"""
class ColegioAdmin(admin.ModelAdmin):
    list_display=['nit', 'nombre', 'tipo', 'jornada', 'year']
    form = forms.ColegioForm

    def get_form(self, request, obj=None, *args, **kwargs):
        if obj:
            kwargs['form']= forms.ColegioFormEdit
        # end if
        return super(ColegioAdmin, self).get_form(request, obj, *args, **kwargs)
    # end def
# end class

exileui.register(models.Sede)
exileui.register(models.Colegio, ColegioAdmin)
