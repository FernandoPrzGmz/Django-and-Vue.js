from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Vacuna(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=70)
    edad = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(150)])
    telefono = models.CharField(max_length=12)
    email = models.EmailField()
    domicilio = models.TextField(null=True, blank=True)

    def __str__(self):
        return F"{self.nombre} {self.apellidos}"


class Mascota(models.Model):

    class Sexo(models.IntegerChoices):
        MASCULINO = 1, 'Masculino'
        FEMENINO = 2, 'Femenino'

    nombre = models.CharField(max_length=50)
    sexo = models.PositiveIntegerField(choices=Sexo.choices)
    edad = models.IntegerField()
    fecha_rescate = models.DateField()
    persona = models.ForeignKey(Persona, null=True, blank=True, on_delete=models.CASCADE)
    vacunas = models.ManyToManyField(Vacuna)

    def __str__(self):
        return self.nombre
