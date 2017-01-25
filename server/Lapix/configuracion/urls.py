from django.conf.urls import include, url
import views

urlpatterns = [
    url(r'^list/sedes/$',
        views.SedesList.as_view(), name="list_sedes"),
]

# Acciones de tipo de Colegio
urlpatterns = [
    url(r'^get/colegio/$',
        views.ColegioType.as_view(), name="get_colegio"),
]
