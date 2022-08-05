from django import forms

from src.apps.refugio.models import Mascota


class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = '__all__'
        widgets = {
            'fecha_rescate': forms.DateInput(attrs={'type': 'date'}),
        }
