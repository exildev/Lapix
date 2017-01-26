from django.conf.urls import include, url
import views

"""
Area
"""
urlpatterns = [
    url(r'^list/areas/$',
        views.AreaList.as_view(), name="list_areas"),
    url(r'^edit/area/(?P<pk>\d+)/$',
        views.AreaForm.as_view(), name="edit_area"),
    url(r'^delete/area/(?P<id>\d+)/$',
        views.delteArea, name="delete_area"),
    url(r'^add/area/$',
        views.AreaForm.as_view(), name="add_area"),
]
