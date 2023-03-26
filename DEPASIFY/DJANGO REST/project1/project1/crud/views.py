from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from project1.crud.serializers import DatosCrudSerializer
from .models import datoscrud


class DatosCrudViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows datosCRUD to be viewed or edited.
    """
    queryset = datoscrud.objects.all().order_by('-FechaHoraCreacion')
    serializer_class = DatosCrudSerializer
    permission_classes = [permissions.IsAuthenticated]

