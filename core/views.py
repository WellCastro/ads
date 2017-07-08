# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import requests
import json

from django.shortcuts import render
from django.views import generic

from property.models import Property
from django.conf import settings

def get_all():
    # get in API properties
    r = requests.get('http://localhost:8000/api/property/all')
    return r.json()

def count_city():
    qs = get_all()
    city_list = []
    city_set = set()
    labels = []

    for i in list(qs):
        value = i.get('city')
        city_list.append(value)
        city_set.add(value)

    for i in city_set:
        labels.append({
                      "city": i.encode("utf-8"),
                      "count": city_list.count(i)
                      })

    return labels

def post_table(data):
    try:
        r = requests.post('http://localhost:8000/api/property/add/', data=data)
    except Exception, e:
        print e
        print r.text
        # log aqui com id
        pass


def populate_table():
    # Property.objects.all().delete()
    path = settings.BASE_DIR + "/utils/seed.json"
    json_file = None
    try:
        with open(path) as json_data:
            json_file = json.load(json_data)
    except Exception, e:
        print e
        pass

    for j in json_file:
        body = {"title": j.get('title'),
                "state": j.get('location').get('city').get('state'),
                "city": j.get('location').get('city').get('name'),
                "name": j.get('location').get('name'),
                "id_json": j.get('id'),
                "purpose": j.get('purpose'),
                "listing_type": j.get('listingType'),
                "published_on": j.get('published_on')}
        post_table(body)
    print body


class Index(generic.TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        # populate_table()
        context["properties"] = get_all()
        context["cities"] = count_city()

        return context

class Api(generic.TemplateView):
    template_name = "doc.html"
