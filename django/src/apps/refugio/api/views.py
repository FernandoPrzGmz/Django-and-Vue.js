from rest_framework import viewsets

from src.apps.refugio.api.serializers import VacunaSerializer, PersonaSerializer, MascotaSerializer
from src.apps.refugio.models import Vacuna, Persona, Mascota


class VacunaViewSet(viewsets.ModelViewSet):
    queryset = Vacuna.objects.all()
    serializer_class = VacunaSerializer


class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer


class MascotaViewSet(viewsets.ModelViewSet):
    queryset = Mascota.objects.prefetch_related('persona', 'vacunas').all()
    serializer_class = MascotaSerializer
