from django.shortcuts import render
from django.utils.decorators import method_decorator
from supra import views as supra
from hojadevida import models
import forms
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
"""
 Issues #6 Servicio lista de profesores
"""
supra.SupraConf.ACCECC_CONTROL["allow"] = True


class ProfesorList(supra.SupraListView):
    model = models.Profesor
    search_key = 'q'
    list_display = ['id', 'nombre', 'identificacion', 'email', 'sexo', 'fecha', 'direccion', 'telefono', 'horario', 'actividades', 'status']
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

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(ProfesorList, self).dispatch(request, *args, **kwargs)
    # end def

    def get_queryset(self):
        queryset = super(ProfesorList, self).get_queryset()
        return queryset
    # end def
# end class


class ProfesorFormEdit(supra.SupraFormView):
    model = models.Profesor
    form_class = forms.EditProfesor

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(ProfesorFormEdit, self).dispatch(request, *args, **kwargs)
    # end def
# end class


class ProfesorFormAdd(supra.SupraFormView):
    model = models.Profesor
    form_class = forms.ProfesorForm

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(ProfesorFormAdd, self).dispatch(request, *args, **kwargs)
    # end def
# end class
