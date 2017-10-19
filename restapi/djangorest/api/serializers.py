# api /serializers.py
from rest_framework import serializers
from .models import Personas

class PersonasSerializer(serializers.ModelSerializer):
    #Serializer para mapear la instancia en un model json

    class Meta:
        #la clase meta mapea los campos
        model = Personas
        fields = ('id', 'name', 'edad', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')
 
