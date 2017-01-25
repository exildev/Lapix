from django.shortcuts import render
from supra import views as supra
from curriculo import models
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


class AreaList(supra.SupraListView):
    model = models.Area
    search_key = "q"
    list_display = ['nombre', 'canhora', 'profesoresList', 'servicios']
    search_fields = ['nombre',]
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
