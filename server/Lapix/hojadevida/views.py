from django.shortcuts import render
from django.utils.decorators import method_decorator
from supra import views as supra
from hojadevida import models
import forms
from http import response
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
"""
 Issues #6 Servicio lista de profesores
"""
supra.SupraConf.ACCECC_CONTROL["allow"] = True


class ProfesorList(supra.SupraListView):
    model = models.Profesor
    search_key = 'q'
    list_display = ['nombre', 'identificacion', 'email', 'sexo', 'fecha', 'direccion', 'telefono', 'horario', 'actividades', 'status', 'servicios']
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
        return queryset.filter(eliminado=False)
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


def deleteProfesor(request, id):
    profesor = models.Profesor.objects.filter(id=id).first()
    if profesor:
        profesor.eliminado = True
        profesor.save()
        return response([], 200)
    # end if
    return response([], 404)
# end def
