# -*- coding: utf-8 -*-
"""Script populate table."""

import requests
import logging
import json

log = logging.getLogger(__name__)

URL = "http://45.55.190.255:8001/api/property"


def post_table(data):
    try:
        requests.post(URL + '/add/', data=data)
    except Exception, e:
        log.error('POST error: %r' % data)
        log.error('Exception error: %r' % e)
        pass


def populate_table():
    path = "./seed.json"
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


if __name__ == '__main__':
    print "==> Populando a base(APENAS IDs não duplicados do arquivo seed.json......"
    populate_table()
    print "==> Base populada........................................................"
