from django.db import models
from aprendices.models import (
    Aprendiz,
)  # Asegúrate de que este sea el nombre correcto de tu app de aprendices


class Equipo(models.Model):
    TIPO_EQUIPO_CHOICES = [
        ("Portátil", "Portátil"),
        ("Escritorio", "Escritorio"),
    ]

    PROCEDENCIA_CHOICES = [
        ("Propio", "Propio"),
        ("SENA", "SENA"),
    ]

    CONDICION_USO_CHOICES = [
        ("Prestado", "Prestado"),
        ("Uso interno", "Uso interno"),
    ]

    tipo_equipo = models.CharField(max_length=20, choices=TIPO_EQUIPO_CHOICES)
    procedencia = models.CharField(max_length=20, choices=PROCEDENCIA_CHOICES)
    condicion_uso = models.CharField(
        max_length=20,
        choices=CONDICION_USO_CHOICES,
        blank=True,
        null=True,
        help_text="Solo aplica si el equipo es del SENA",
    )
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    numero_serie = models.CharField(max_length=50, unique=True, null=True)
    observaciones = models.TextField(blank=True, null=True)
    aprendiz = models.ForeignKey(
        Aprendiz, on_delete=models.CASCADE, related_name="equipos"
    )

    def __str__(self):
        return f"{self.tipo_equipo} - {self.marca} {self.modelo} ({self.numero_serie})"
