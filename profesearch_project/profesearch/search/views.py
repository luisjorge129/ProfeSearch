# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import TemplateView
import urllib
import requests

apiUrl = "https://notaso.com/api/"


class SearchView(TemplateView):
    template_name = 'search/search.html'
    queryset = ""


class ProfessorsListView(ListView):
    template_name = 'search/professorsList.html'
    queryset = ""

    def get_context_data(self, **kwargs):
        context = super(ProfessorsListView, self).get_context_data(**kwargs)
        q = self.request.GET.get('q')
        # url = self.request.GET.get('url')
        # if url:
        #     url = url + "&page=%s&json=%s" % (self.request.GET.get('page'),
        #                                       self.request.GET.get('format'))
        #     listings = json.load(urllib2.urlopen(url))
        #     for result in listings['results']:
        #         result['star_score'] = starScore(result['score']*100)
        #     context['professorsList'] = listings
        #     context['keyword'] = q
        if q:
            payload = {"format": "json",
                       "q": q}
            listings = requests.get(apiUrl + "search/", params=payload).json()
            for result in listings['results']:
                result['star_score'] = starScore(result['score']*100)
            context['professorsList'] = listings
            context['keyword'] = q
        return context


class ProfessorDetailView(TemplateView):
    template_name = 'search/professorDetail.html'

    def get_context_data(self, id, **kwargs):
        context = super(ProfessorDetailView, self).get_context_data(**kwargs)
        if 'view' not in kwargs:
            kwargs['view'] = self

        id = self.kwargs['id']
        if id:
            payload = {"format": "json", "comments": "true"}
            result = (requests.get(apiUrl + "professors/"
                                   + id, params=payload).json())
            context['professor'] = result
            context['star_score'] = starScore(result['score']*100)
        return context


#Get star score
def starScore(score):
    if score <= 100:
        star = 5
    if score <= 90:
        star = 4
    if score <= 80:
        star = 3
    if score <= 70:
        star = 2
    if score <= 60:
        star = 1
    return star
