from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns(
    '',
    url(r'^$', views.HomeView.as_view(), name="home"),
    url(r'^search$', views.ProfessorsListView.as_view(),
        name="professor-list"),
    url(r'^professor/(?P<id>\d+)$', views.ProfessorDetailView.as_view(),
        name="professor-detail"),
)
