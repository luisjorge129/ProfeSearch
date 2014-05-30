from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import TemplateView
import json
import urllib2
import urllib

uri = "https://notaso.com/api/"


class HomeView(TemplateView):
    template_name = 'home/home.html'
    queryset = ""


class ProfessorsListView(ListView):
    template_name = 'home/professorsList.html'
    queryset = ""

    def get_context_data(self, **kwargs):
        context = super(ProfessorsListView, self).get_context_data(**kwargs)
        q = self.request.GET.get('q')
        if q:
            url = uri + "search/?format=%s&q=%s" % ("json",
                                                    urllib.quote_plus(q))
            results = json.load(urllib2.urlopen(url))
            for result in results:
                result['star_score'] = starScore(0.40*100)
            context['professorsList'] = results
            context['count'] = len(results)
            context['keyword'] = q
        elif q == "":
            context['count'] = ""
        return context


class ProfessorDetailView(TemplateView):
    template_name = 'home/professorDetail.html'

    def get_context_data(self, id, **kwargs):
        context = super(ProfessorDetailView, self).get_context_data(**kwargs)
        if 'view' not in kwargs:
            kwargs['view'] = self

        id = self.kwargs['id']
        if id:
            url = uri + "professors/%s?format=%s&comments=%s" % (id, "json",
                                                                 "true")
            result = json.load(urllib2.urlopen(url))
            context['professor'] = result
            context['star_score'] = starScore(result['score']*100)
            print context['star_score']
        return context


#Get star score
def starScore(score):
    if score >= 90:
        star = 5
    if score >= 80:
        star = 4
    if score >= 70:
        star = 3
    if score >= 60:
        star = 2
    if score < 60:
        star = 1
    return star
