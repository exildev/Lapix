from django.shortcuts import render
from supra import views as supra
from curriculo import models
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def deleteFactory(id, tipo):
    if tipo == 1:
        obj = models.Area.objects.filter(id=id).first()
    elif tipo == 2:
        obj = models.Materia.objects.filter(id=id).first()
    elif tipo == 3:
        obj = models.Grado.objects.filter(id=id).first()
    elif tipo == 4:
        obj = models.Curso.objects.filter(id=id).first()
    # end if
    if obj:
        obj.eliminado = True
        obj.save()
        return response([], 200)
    # end if
    return response([], 404)
# end def


class AreaList(supra.SupraListView):
    model = models.Area
    search_key = "q"
    list_filter = ['id', ]
    list_display = ['nombre', 'canhora', 'profesoresList', 'servicios']
    search_fields = ['nombre', ]
    paginate_by = 10

    def servicios(self, obj, row):
        edit = "/curriculo/edit/area/%d/" % (obj.id)
        delete = "/curriculo/delete/area/%d/" % (obj.id)
        return {'add': '/curriculo/add/area/', 'edit': edit, 'delete': delete}
    # end def

    def profesoresList(self, obj, row):
        lista = []
        for p in obj.profesores:
            lista.append({'nombre': p.first_name, 'apellidos': p.last_name})
        return lista
    # end def

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(AreaList, self).dispatch(request, *args, **kwargs)
    # end def

    def get_queryset(self):
        queryset = super(AreaList, self).get_queryset()
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


class AreaForm(supra.SupraFormView):
    model = models.Area
    response_json = False

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(AreaForm, self).dispatch(request, *args, **kwargs)
    # end def
# end class


def delteArea(request, id):
    return deleteFactory(id, 1)
# end def
