from rest_framework import serializers

from src.apps.refugio import models


class VacunaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vacuna
        fields = '__all__'


class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Persona
        fields = '__all__'


class MascotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Mascota
        fields = '__all__'

    def to_representation(self, instance):
        self.fields['persona'] = PersonaSerializer()
        self.fields['vacunas'] = VacunaSerializer(many=True)
        return super(MascotaSerializer, self).to_representation(instance)
