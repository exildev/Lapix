from django.conf.urls import include, url
import views

"""
Area
"""
urlpatterns = [
    url(r'^list/areas/$',
        views.AreaList.as_view(), name="list_areas"),
]
