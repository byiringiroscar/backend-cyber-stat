from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializer import InformationSerializer


# Create your views here.


class InformationListCreateAPIView(ListCreateAPIView):
    serializer_class = InformationSerializer
    queryset = InformationSerializer.Meta.model.objects.all()


class InformationRetrieveUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = InformationSerializer
    queryset = InformationSerializer.Meta.model.objects.all()
    lookup_field = 'id'
