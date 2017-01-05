from django.conf.urls import include, url
import views

urlpatterns = [
    url(r'^list/profesores/$',
        views.ProfesorList.as_view(), name="list_profesores"),
    url(r'^edit/profesor/(?P<pk>\d+)/$',
        views.ProfesorFormEdit.as_view(), name="edit_profesor"),
    url(r'^delete/profesor/(?P<id>\d+)/$',
        views.deleteProfesor, name="delete_profesor"),
    url(r'^add/profesor/$',
        views.ProfesorFormAdd.as_view(), name="add_profesor"),
]
