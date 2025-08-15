from django import forms
from .models import Equipo


class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = [
            "tipo_equipo",
            "procedencia",
            "condicion_uso",
            "marca",
            "modelo",
            "numero_serie",
            "observaciones",
            "aprendiz",
        ]
        widgets = {
            "tipo_equipo": forms.Select(attrs={"class": "form-select"}),
            "procedencia": forms.Select(attrs={"class": "form-select"}),
            "condicion_uso": forms.Select(attrs={"class": "form-select"}),
            "marca": forms.TextInput(attrs={"class": "form-control"}),
            "modelo": forms.TextInput(attrs={"class": "form-control"}),
            "numero_serie": forms.TextInput(attrs={"class": "form-control"}),
            "observaciones": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
            "aprendiz": forms.Select(attrs={"class": "form-select"}),
        }
