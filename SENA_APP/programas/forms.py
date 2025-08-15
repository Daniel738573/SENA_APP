from django import forms
from .models import Programa


class ProgramaForm(forms.Form):
    codigo = forms.IntegerField(label="Código del Programa")
    nombre = forms.CharField(max_length=200, label="Nombre del Programa")
    nivel_formacion = forms.CharField(max_length=100, label="Nivel de Formación")
    modalidad = forms.CharField(max_length=100, label="Modalidad")
    duracion_meses = forms.IntegerField(label="Duración en Meses", min_value=6)
    duracion_horas = forms.IntegerField(label="Duración en Horas", min_value=40)
    descripcion = forms.CharField(
        widget=forms.Textarea, label="Descripción del Programa"
    )
    competencias = forms.CharField(
        widget=forms.Textarea, label="Competencias a Desarrollar"
    )
    perfil_egreso = forms.CharField(widget=forms.Textarea, label="Perfil de Egreso")
    requisitos_ingreso = forms.CharField(
        widget=forms.Textarea, label="Requisitos de Ingreso"
    )
    centro_formacion = forms.CharField(max_length=200, label="Centro de Formación")
    regional = forms.CharField(max_length=100, label="Regional")
    estado = forms.CharField(max_length=50, label="Estado")
    fecha_creacion = forms.DateField(label="Fecha de Creación")
    fecha_registro = forms.DateTimeField(label="Fecha de Registro")

    def clean(self):
        cleaned_data = super().clean()
        if not cleaned_data.get("codigo") or not cleaned_data.get("nombre"):
            raise forms.ValidationError("Código y nombre son obligatorios.")
        return cleaned_data

    def clean_codigo(self):
        codigo = self.cleaned_data["codigo"]
        if codigo <= 0:
            raise forms.ValidationError("El código debe ser un número positivo.")
        return codigo

    def save(self):
        """Guarda el programa en la base de datos"""
        try:
            programa = Programa.objects.create(
                codigo=self.cleaned_data["codigo"],
                nombre=self.cleaned_data["nombre"],
                nivel_formacion=self.cleaned_data["nivel_formacion"],
                modalidad=self.cleaned_data["modalidad"],
                duracion_meses=self.cleaned_data["duracion_meses"],
                duracion_horas=self.cleaned_data["duracion_horas"],
                descripcion=self.cleaned_data["descripcion"],
                competencias=self.cleaned_data["competencias"],
                perfil_egreso=self.cleaned_data["perfil_egreso"],
                requisitos_ingreso=self.cleaned_data["requisitos_ingreso"],
                centro_formacion=self.cleaned_data["centro_formacion"],
                regional=self.cleaned_data["regional"],
                estado=self.cleaned_data["estado"],
                fecha_creacion=self.cleaned_data["fecha_creacion"],
                fecha_registro=self.cleaned_data["fecha_registro"],
            )
            return programa
        except Exception as e:
            raise forms.ValidationError(f"Error al crear el programa: {str(e)}")
