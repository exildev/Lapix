from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator
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
    list_display = ['nombre', 'identificacion', 'email', 'sexo', 'fecha', 'direccion', 'telefono', 'horario', 'actividades', 'status', 'servicios', 'imagen', 'hoja_vida']
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


class ProfesorFormEdit(supra.SupraFormView):
    model = models.Profesor
    form_class = forms.EditProfesor
    response_json = False

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(ProfesorFormEdit, self).dispatch(request, *args, **kwargs)
    # end def
# end class


class ProfesorFormAdd(supra.SupraFormView):
    model = models.Profesor
    form_class = forms.ProfesorForm
    response_json = False

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


class EstudianteList(supra.SupraListView):
    model = models.Estudiante
    search_key = 'q'
    list_display = ['nombre', 'identificacion', 'email', 'sexo', 'fecha', 'direccion', 'telefono', 'grado', 'status', 'servicios', 'grado', 'imagen', 'codigo_Estudiante', 'colegio_Anterior']
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
    estudiante = models.Estudiante.objects.filter(id=id).first()
    if estudiante:
        estudiante.eliminado = True
        estudiante.save()
        return response([], 200)
    # end if
    return response([], 404)
# end def


class AcudienteList(supra.SupraListView):
    model = models.Acudiente
    search_key = 'q'
    list_display = ['nombre', 'identificacion', 'email', 'sexo', 'fecha', 'direccion', 'telefono', 'status', 'servicios', 'imagen']
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
    acudiente = models.Acudiente.objects.filter(id=id).first()
    if acudiente:
        acudiente.eliminado = True
        acudiente.save()
        return response([], 200)
    # end if
    return response([], 404)
# end def
