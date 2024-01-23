from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializer import InformationSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *


# Create your views here.


class InformationListCreateAPIView(ListCreateAPIView):
    serializer_class = InformationSerializer
    queryset = InformationSerializer.Meta.model.objects.all()


class InformationRetrieveUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = InformationSerializer
    queryset = InformationSerializer.Meta.model.objects.all()
    lookup_field = 'id'


@api_view(['GET', ])
def get_country(request, country):
    country = str(country.lower())
    try:
        country = Information.objects.filter(country=country)
    except InformationSerializer.Meta.model.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = InformationSerializer(country, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
