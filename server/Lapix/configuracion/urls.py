from django.conf.urls import include, url
import views

urlpatterns = [
    url(r'^list/sedes/$',
        views.SedesList.as_view(), name="list_sedes"),
]
