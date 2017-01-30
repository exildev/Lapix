from django.conf.urls import include, url
import views

urlpatterns = [
    url(r'^list/sedes/$',
        views.SedesList.as_view(), name="list_sedes"),
]

# Acciones de tipo de Colegio
urlpatterns = [
    url(r'^get/colegio/$',#muestra la configuracion del tipo de colegio
        views.ColegioType.as_view(), name="get_colegio"),
]

# Acciones de tipo de Sede
urlpatterns = [
    url(r'^add/sede/$',
        views.SedeFormView.as_view(), name="add_sede"),
    url(r'^edit/sede/(?P<pk>\d+)/$',
        views.SedeFormView.as_view(), name="edit_sede"),
    url(r'^delete/sede/(?P<pk>\d+)/$',
        views.SedeFormView.as_view(), name="edit_sede"),
]


# Acciones de Jornada
urlpatterns = [
    url(r'^list/jornada/$',
        views.JornadaList.as_view(), name="list_jornada"),
]
