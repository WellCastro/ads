# -*- coding: utf-8 -*-
import sys
import logging

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Property
from .serializers import PropertySerializer
from rest_framework.pagination import PageNumberPagination

log = logging.getLogger(__name__)

reload(sys)
sys.setdefaultencoding('utf8')


class ItemsSetPagination(PageNumberPagination):
    # config page size
    page_size = 100


# View property.
class PropertyView(APIView):
    # url: api/property/
    def get(self, request, id=None, format=None):
        search = request.query_params.get('search')
        log.info('List: %r' % id)

        if id == 'all':
            qs = Property.objects.all()
        elif search:
            qs = Property.objects.filter(title__contains=search)
        else:
            qs = Property.objects.filter(id_json=id)

        # control pagination
        pagination_class = ItemsSetPagination
        paginator = pagination_class()
        page = paginator.paginate_queryset(qs, request)

        serializer = PropertySerializer(page, many=True)

        return paginator.get_paginated_response(serializer.data)

    # url: api/property/add/
    def post(self, request, format=None):
        serializer = PropertySerializer(data=request.data)
        log.info('POST: %r' % request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        log.error('POST BAD request: %r' % request.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # url: api/property/remove/id
    def delete(self, request, id, format=None):
        print id
        try:
            qs = Property.objects.get(id_json=id)
            qs.delete()
            resp_status = status.HTTP_200_OK
        except:
            log.error('DEL NOT FOUND: %r' % id)
            resp_status = status.HTTP_404_NOT_FOUND
            pass

        return Response(resp_status, status=resp_status)

    def put(self, request, id, format=None):
        qs = Property.objects.get(id_json=id)
        serializer = PropertySerializer(qs, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        log.error('PUT BAD request: %r' % request.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
