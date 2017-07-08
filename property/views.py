# -*- coding: utf-8 -*-
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Property
from .serializers import PropertySerializer


# View property.
class PropertyView(APIView):
    # url: api/property/
    def get(self, request, id=None, format=None):
        if id == 'all':
            qs = Property.objects.all()
        else:
            qs = Property.objects.filter(id_json=id)
        serializer = PropertySerializer(qs, many=True)

        return Response(serializer.data)

    # url: api/property/add/
    def post(self, request, format=None):
        serializer = PropertySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # url: api/property/remove/id
    def delete(self, request, id, format=None):
        try:
            qs = Property.objects.get(id_json=id)
            qs.delete()
            resp_status = status.HTTP_200_OK
        except:
            resp_status = status.HTTP_404_NOT_FOUND
            pass

        return Response(resp_status, status=resp_status)