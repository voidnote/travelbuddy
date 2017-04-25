from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<userid>\d+)/(?P<route>\w+)$', views.travels),
    url(r'^addplan/(?P<id>\d+)$', views.addplan, name = "my_addplan"),
    url(r'^createplan/(?P<id>\d+)$', views.createPlan, name = "my_createplan"),
    url(r'^join/(?P<userid>\d+)/(?P<tripid>\d+)$', views.joinTrip, name = "my_join"),
    url(r'^destination/(?P<tripid>\d+)$', views.destination, name = "my_destination"),
]
