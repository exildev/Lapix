from django.shortcuts import render, redirect, HttpResponse
from configuracion.models import Sede
from supra import views as supra
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import datetime
import models
import forms
from django.views.generic.base import View
from Lapix.settings import MOD_CONFIGURACION
# Create your views here.


class InfoSede(supra.SupraListView):
    model = Sede
    search_key = 'q'
    list_display = ['nombre', 'registro', 'direccion', 'estado']
    search_fields = ['id', 'nombre', 'direccion', 'registro']
    paginate_by = 1

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(InfoSede, self).dispatch(request, *args, **kwargs)
    # end def
# end class

class SedesList(supra.SupraListView):
    model = Sede
    search_key = 'q'
    list_display = ['nombre', 'registro', 'direccion', 'estado', 'servicios']
    search_fields = ['nombre', 'direccion', 'registro']

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(SedesList, self).dispatch(request, *args, **kwargs)
    # end def

    def get_queryset(self):
        queryset = super(SedesList , self).get_queryset()
        self.paginate_by = self.request.GET.get('num_page', False)
        propiedad = self.request.GET.get('sort_property', False)
        orden = self.request.GET.get('sort_direction', False)
        queryset2 = queryset.filter(estado=True)
        if propiedad and orden:
            if orden == "asc":
                queryset2 = queryset2.order_by(propiedad)
            elif orden == "desc":
                propiedad = "-"+propiedad
                queryset2 = queryset2.order_by(propiedad)
        # end if
        return queryset2
    # end def

    def servicios(self, obj, row):
        edit = "/%s/edit/sede/%d/" % (MOD_CONFIGURACION, obj.id)
        delete = "/%s/delete/sede/%d/" % (MOD_CONFIGURACION, obj.id)
        return {'add': '/%s/add/sede/'%(MOD_CONFIGURACION), 'edit': edit, 'delete': delete}
    # end def
# end class

class BuilderDelete():
    @staticmethod
    def eraseObjeto(pk, op):
        if op == 1:
            obj = models.Sede.objects.filter(id=pk, estado=True).first()
        #end if
        if obj :
            obj.estado=False
            obj.save()
            return 'Ok', 200
        # end if
        return 'NOT', 404
    # end def
# end class

class ColegioType(supra.SupraListView):
    model = models.Colegio
    list_display = ['tipo', 'jornada']

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(ColegioType, self).dispatch(request, *args, **kwargs)
    # end def

    def get_queryset(self):
        query = super(ColegioType, self).get_queryset()
        return query.filter(year=datetime.datetime.now().year)
    # end def
# end class


class SedeFormView(supra.SupraFormView):
    model = models.Sede
    template_name = 'configuracion/addSede.html'
    form_class = forms.SedeForm
# end class


class DeleteSede(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        print args,kwargs
        respuesta, status= BuilderDelete.eraseObjeto(kwargs['pk'], 1)
        return HttpResponse(respuesta, content_type="application/json", status=status)
    # end def
# end def

class JornadaList(supra.SupraListView):
    model = models.Configuracion
    list_display = ['sede', 'jornada','horaIni','fin']
    search_key = 'q'
    search_fields = ['id']

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(JornadaList, self).dispatch(request, *args, **kwargs)
    # end def
# end class


class JornadaFormView(supra.SupraFormView):
    model = models.Configuracion
    template_name = 'configuracion/addJornada.html'
    form_class = forms.JornadaForm
# end class
