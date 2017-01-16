from django.shortcuts import render
from configuracion.models import Sede
from supra import views as supra
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

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
