from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import datoscrud


class DatosCrudSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = datoscrud
        fields = ['id','Nombre', 'Apellidos', 'Calificacion', 'FechaHoraCreacion']
        read_only_fields= ['FechaHoraCreacion',]

