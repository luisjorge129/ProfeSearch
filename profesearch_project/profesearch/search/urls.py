from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns(
    '',
    url(r'^$', views.SearchView.as_view(), name="search"),
    url(r'^search$', views.ProfessorsListView.as_view(),
        name="professor-list"),
    url(r'^professor/(?P<id>\d+)$', views.ProfessorDetailView.as_view(),
        name="professor-detail"),
)
