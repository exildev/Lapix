from django.conf.urls import include, url
import views

urlpatterns = [
    url(r'^list/sedes/$',
        views.SedesList.as_view(), name="list_sedes"),
]

# Acciones de tipo de Colegio
urlpatterns += [
    url(r'^get/colegio/$',#muestra la configuracion del tipo de colegio
        views.ColegioType.as_view(), name="get_colegio"),
]

# Acciones de tipo de Sede
urlpatterns += [
    url(r'^add/sede/$',
        views.SedeFormView.as_view(), name="add_sede"),
    url(r'^edit/sede/(?P<pk>\d+)/$',
        views.SedeFormView.as_view(), name="edit_sede"),
    url(r'^delete/sede/(?P<pk>\d+)/$',
        views.DeleteSede.as_view(), name="delete_sede"),
    url(r'^info/sede/$',
        views.InfoSede.as_view(), name="info_sede"),
]


# Acciones de Jornada
urlpatterns += [
    url(r'^list/jornada/$',
        views.JornadaList.as_view(), name="list_jornada"),
    url(r'^add/jornada/$',
        views.JornadaFormView.as_view(), name="add_jornada"),
    url(r'^edit/jornada/(?P<pk>\d+)/$',
        views.JornadaFormView.as_view(), name="edit_jornada"),
    url(r'^info/jornada/$',
        views.InfoSede.as_view(), name="info_jornada"),
    url(r'^delete/jornada/(?P<pk>\d+)/$',
        views.DeleteJornada.as_view(), name="delate_jornada"),
]
