from django.urls import path
from . import views

app_name = "equipos"  # <- imprescindible para el namespace

urlpatterns = [
    path("", views.lista_equipos, name="lista_equipos"),
    path("crear/", views.crear_equipo, name="crear_equipo"),
    path("<int:pk>/", views.detalle_equipo, name="detalle_equipo"),
    path("<int:pk>/editar/", views.editar_equipo, name="editar_equipo"),
    path("<int:pk>/eliminar/", views.eliminar_equipo, name="eliminar_equipo"),
]
