# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views import generic

from property.models import Property

import requests

def get_all():
    # get in API properties all
    r = requests.get('http://localhost:8000/api/property/all')
    return r.json()

class Index(generic.TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context["properties"] = get_all()

        return context
