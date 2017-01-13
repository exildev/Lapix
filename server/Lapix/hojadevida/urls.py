from django.conf.urls import include, url
import views

"""
Profesor
"""
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

"""
Estudiante
"""
urlpatterns += [
    url(r'^list/estudiantes/$',
        views.EstudianteList.as_view(), name="list_estudiantes"),
    url(r'^edit/estudiante/(?P<pk>\d+)/$',
        views.EstudianteFormEdit.as_view(), name="edit_estudiante"),
    url(r'^delete/estudiante/(?P<id>\d+)/$',
        views.deleteEstudiante, name="delete_estudiante"),
    url(r'^add/estudiante/$',
        views.EstudianteFormAdd.as_view(), name="add_estudiante"),
]

"""
Acudiente
"""
urlpatterns += [
    url(r'^list/acudiente/$',
        views.AcudienteList.as_view(), name="list_acudientes"),
    url(r'^edit/acudiente/(?P<pk>\d+)/$',
        views.AcudienteFormEdit.as_view(), name="edit_acudiente"),
    url(r'^delete/acudiente/(?P<id>\d+)/$',
        views.deleteAcudiente, name="delete_estudiante"),
    url(r'^add/acudiente/$',
        views.AcudienteFormAdd.as_view(), name="add_acudiente"),
]
