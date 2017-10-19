# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.

SEXOS = (("M","Mujer"),("H","Hombre"),("I","Indefinido"))
TIPOPERSONA = (("Voluntario","Voluntario"),("Damnificado","Damnificado"),("Otro","Otro"))

# Model Personas
class Personas(models.Model):
    #pass
    name = models.CharField(max_length=255, blank=False, unique=True)
    edad = models.IntegerField()
    sexo =  models.CharField(max_length=100)
    tipo_de_persona = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        #Return a human readable representation of the model instance.
        return "{}".format(self.name)
