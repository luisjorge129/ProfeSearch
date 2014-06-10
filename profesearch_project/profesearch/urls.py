from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    '',
    url(r'^', include('profesearch_project.profesearch.home.urls',
        namespace="home")),
)
