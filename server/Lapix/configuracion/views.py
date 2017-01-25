from django.shortcuts import render
from configuracion.models import Sede
from supra import views as supra
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import datetime
import models
import forms
# Create your views here.


class SedesList(supra.SupraListView):
    model = Sede
    search_key = 'q'
    list_display = ['nombre', 'registro', 'direccion', 'estado']
    search_fields = ['nombre', 'direccion', 'registro']

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(SedesList, self).dispatch(request, *args, **kwargs)
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
