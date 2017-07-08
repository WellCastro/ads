# -*- coding: utf-8 -*-
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Property
from .serializers import PropertySerializer


# View property.
class PropertyView(APIView):
    # url: property/
    def get(self, request, format=None):
            qs = Property.objects.all()
            serializer = PropertySerializer(qs, many=True)

            return Response(serializer.data)

    # url: property/add/
    def post(self, request, format=None):
        serializer = PropertySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
