# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import generics
from .serializers import PersonasSerializer
from .models import Personas
#from django.shortcuts import render

# Create your views here.
class CreateView(generics.ListCreateAPIView):
    queryset = Personas.objects.all()
    serializer_class = PersonasSerializer

    def perform_create(self, serializer):
        serializer.save()

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = Personas.objects.all()
    serializer_class = PersonasSerializer
