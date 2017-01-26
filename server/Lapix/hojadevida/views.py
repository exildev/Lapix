#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth import login, logout, authenticate
from supra import views as supra
from hojadevida import models
import forms
import json as simplejson
from http import response
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
"""
 Issues #6 Servicio lista de profesores
"""
supra.SupraConf.ACCECC_CONTROL["allow"] = True


def deleteFactory(id, tipo):
    if tipo == 1:
        obj = models.Profesor.objects.filter(id=id).first()
    elif tipo == 2:
        obj = models.Estudiante.objects.filter(id=id).first()
    elif tipo == 3:
        obj = models.Acudiente.objects.filter(id=id).first()
    # end if
    if obj:
        obj.eliminado = True
        obj.save()
        return response([], 200)
    # end if
    return response([], 404)
# end def


class ProfesorList(supra.SupraListView):
    model = models.Profesor
    search_key = 'q'
    list_filter = ['asignacionsede__sede',]
    list_display = ['nombre', 'identificacion', 'email', 'sexo', 'date', 'direccion', 'telefono', 'horario', 'actividades', 'status', 'servicios', 'sedes', 'imagen', 'hoja_vida', 'id']
    search_fields = ['first_name', 'last_name', 'identificacion']
    paginate_by = 10

    def nombre(self, obj, row):
        return {'first_name': obj.first_name, 'last_name':obj.last_name }
    # end def

    def horario(self, obj, row):
        return "/horario/profesor/%d/" % (obj.id)
    # end def

    def actividades(self, obj, row):
        return "/actividades/profesor/%d/" % (obj.id)
    # end def

    def date(self, obj, row):
        return obj.fecha.strftime("%Y-%m-%d")
    # end def

    def sedes(self, obj, row):
        asiganacion = models.AsignacionSede.objects.filter(profesor=obj.id)
        return list(asiganacion.values('sede', 'sede__nombre', 'id'))
    # end def

    def servicios(self, obj, row):
        edit = "/usuarios/edit/profesor/%d/" % (obj.id)
        delete = "/usuarios/delete/profesor/%d/" % (obj.id)
        return {'add': '/usuarios/add/profesor/', 'edit': edit, 'delete': delete}
    # end def

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(ProfesorList, self).dispatch(request, *args, **kwargs)
    # end def

    def get_queryset(self):
        queryset = super(ProfesorList, self).get_queryset()
        self.paginate_by = self.request.GET.get('num_page', False)
        propiedad = self.request.GET.get('sort_property', False)
        orden = self.request.GET.get('sort_direction', False)
        queryset2 = queryset.filter(eliminado=False)
        if propiedad and orden:
            if orden == "asc":
                queryset2 = queryset2.order_by(propiedad)
            elif orden == "desc":
                propiedad = "-"+propiedad
                queryset2 = queryset2.order_by(propiedad)
        # end if
        return queryset2
    # end def
# end class


class AsignacionSedeInline(supra.SupraInlineFormView):
    base_model = models.Profesor
    model = models.AsignacionSede
    form_class = forms.AsignacionSedeForm
# end class


class ProfesorFormEdit(supra.SupraFormView):
    model = models.Profesor
    form_class = forms.EditProfesor
    inlines = [AsignacionSedeInline]
    response_json = False

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(ProfesorFormEdit, self).dispatch(request, *args, **kwargs)
    # end def
# end class


class ProfesorFormAdd(supra.SupraFormView):
    model = models.Profesor
    form_class = forms.ProfesorForm
    inlines = [AsignacionSedeInline]
    response_json = False

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(ProfesorFormAdd, self).dispatch(request, *args, **kwargs)
    # end def
# end class


def deleteProfesor(request, id):
    return deleteFactory(id, 1)
# end def


class EstudianteList(supra.SupraListView):
    model = models.Estudiante
    search_key = 'q'
    list_display = ['nombre', 'identificacion', 'email', 'sexo', 'date', 'direccion', 'telefono', 'grado', 'status', 'servicios', 'grado', 'imagen', 'codigo_Estudiante', 'colegio_Anterior', 'id']
    search_fields = ['first_name', 'last_name', 'identificacion']
    paginate_by = 10

    def nombre(self, obj, row):
        return {'first_name': obj.first_name, 'last_name':obj.last_name }
    # end def

    def servicios(self, obj, row):
        edit = "/usuarios/edit/estudiante/%d/" % (obj.id)
        delete = "/usuarios/delete/estudiante/%d/" % (obj.id)
        return {'add': '/usuarios/add/estudiante/', 'edit': edit, 'delete': delete}
    # end def

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(EstudianteList, self).dispatch(request, *args, **kwargs)
    # end def

    def date(self, obj, row):
        return obj.fecha.strftime("%Y-%m-%d")
    # end def

    def get_queryset(self):
        queryset = super(EstudianteList, self).get_queryset()
        self.paginate_by = self.request.GET.get('num_page', False)
        propiedad = self.request.GET.get('sort_property', False)
        orden = self.request.GET.get('sort_direction', False)
        queryset2 = queryset.filter(eliminado=False)
        if propiedad and orden:
            if orden == "asc":
                queryset2 = queryset2.order_by(propiedad)
            elif orden == "desc":
                propiedad = "-"+propiedad
                queryset2 = queryset2.order_by(propiedad)
        # end if
        return queryset2
    # end def
# end class


class EstudianteFormEdit(supra.SupraFormView):
    model = models.Estudiante
    form_class = forms.EdirEstudiante
    response_json = False

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(EstudianteFormEdit, self).dispatch(request, *args, **kwargs)
    # end def
# end class


class EstudianteFormAdd(supra.SupraFormView):
    model = models.Estudiante
    form_class = forms.EstudianteForm
    response_json = False

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(EstudianteFormAdd, self).dispatch(request, *args, **kwargs)
    # end def
# end class


def deleteEstudiante(request, id):
    return deleteFactory(id, 2)
# end def


class GradosAnterioresList(supra.SupraListView):
    model = models.GradoEntrante
    list_display = ['nombre', 'id']

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(GradosAnterioresList, self).dispatch(request, *args, **kwargs)
    # end def
# end class


class AcudienteList(supra.SupraListView):
    model = models.Acudiente
    search_key = 'q'
    list_filter = ['asignacionsede__sede',]
    list_display = ['nombre', 'identificacion', 'email', 'sexo', 'date', 'direccion', 'telefono', 'status', 'servicios', 'imagen', 'id']
    search_fields = ['first_name', 'last_name', 'identificacion']
    paginate_by = 10

    def nombre(self, obj, row):
        return {'first_name': obj.first_name, 'last_name':obj.last_name }
    # end def

    def servicios(self, obj, row):
        edit = "/usuarios/edit/acudiente/%d/" % (obj.id)
        delete = "/usuarios/delete/acudiente/%d/" % (obj.id)
        return {'add': '/usuarios/add/acudiente/', 'edit': edit, 'delete': delete}
    # end def

    def date(self, obj, row):
        return obj.fecha.strftime("%Y-%m-%d")
    # end def

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(AcudienteList, self).dispatch(request, *args, **kwargs)
    # end def

    def get_queryset(self):
        queryset = super(AcudienteList, self).get_queryset()
        self.paginate_by = self.request.GET.get('num_page', False)
        propiedad = self.request.GET.get('sort_property', False)
        orden = self.request.GET.get('sort_direction', False)
        queryset2 = queryset.filter(eliminado=False)
        if propiedad and orden:
            if orden == "asc":
                queryset2 = queryset2.order_by(propiedad)
            elif orden == "desc":
                propiedad = "-"+propiedad
                queryset2 = queryset2.order_by(propiedad)
        # end if
        return queryset2
    # end def
# end class


class AcudienteFormEdit(supra.SupraFormView):
    model = models.Acudiente
    form_class = forms.EditAcudiente
    response_json = False

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(AcudienteFormEdit, self).dispatch(request, *args, **kwargs)
    # end def
# end class


class AcudienteFormAdd(supra.SupraFormView):
    model = models.Acudiente
    form_class = forms.AcudienteForm
    response_json = False

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(AcudienteFormAdd, self).dispatch(request, *args, **kwargs)
    # end def
# end class


def deleteAcudiente(request, id):
    return deleteFactory(id, 3)
# end def


"""
    Logins
"""


@csrf_exempt
def loginU(request):
    if request.method == "POST":
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            usuario = authenticate(username=username, password=password)
            if usuario is not None:
                if usuario.is_active:
                    login(request, usuario)
                    return response(simplejson.dumps({"exito": ["Usuario Conectado"]}), 200)
                # end if
                return response(simplejson.dumps({"error": ["Usuario desactivado"]}), 400)
            # end if
            return response(simplejson.dumps({"error": ["Usuario o contraseña incorrectos"]}), 400)
        # end if
        errors = form.errors.items()
        return response(simplejson.dumps(dict(errors)), 400)
    # end if
    return response([], 403)
# end def


class LoginA(supra.SupraSession):
    model = models.Acudiente

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(LoginA, self).dispatch(request, *args, **kwargs)
    # end def
# end class


class LoginE(supra.SupraSession):
    model = models.Estudiante

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(LoginE, self).dispatch(request, *args, **kwargs)
    # end def
# end class


class LoginP(supra.SupraSession):
    model = models.Profesor

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(LoginP, self).dispatch(request, *args, **kwargs)
    # end def
# end class


def logoutU(request):
    logout(request)
    return response([], 200)
# end def
