from django.db import models


class Instructor(models.Model):
    TIPO_DOCUMENTO_CHOICES = [
        ("CC", "Cédula de Ciudadanía"),
        ("CE", "Cédula de Extranjería"),
        ("TI", "Tarjeta de Identidad"),
        ("PAS", "Pasaporte"),
    ]
    NIVEL_EDUCATIVO_CHOICES = [
        ("TEC", "Técnico"),
        ("TGL", "Tecnólogo"),
        ("PRE", "Pregrado"),
        ("ESP", "Especialización"),
        ("MAE", "Maestría"),
        ("DOC", "Doctorado"),
    ]

    documento_identidad = models.IntegerField(max_length=20, unique=True)
    tipo_documento = models.CharField(
        max_length=3, choices=TIPO_DOCUMENTO_CHOICES, default="CC"
    )
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.IntegerField(max_length=20, null=True)
    correo = models.EmailField(max_length=100, null=True)
    fecha_nacimiento = models.DateField()
    ciudad = models.CharField(max_length=100, null=True)
    direccion = models.TextField(max_length=100, null=True)
    nivel_educativo = models.CharField(
        max_length=3, choices=NIVEL_EDUCATIVO_CHOICES, default="MAE"
    )
    especialidad = models.CharField(max_length=100)
    anios_experiencia = models.PositiveIntegerField()
    activo = models.BooleanField(default=True)
    fecha_vinculacion = models.DateField()


def __str__(self):
    return f"{self.nombre} {self.apellido} - {self.documento_identidad}"


def nombre_completo(self):
    return f"{self.nombre} {self.apellido}"
