from django.shortcuts import render, get_object_or_404, redirect
from .models import Equipo
from .forms import EquipoForm


# LISTA
def lista_equipos(request):
    equipos = Equipo.objects.all().order_by("id")
    form = EquipoForm()
    if request.method == "POST":
        form = EquipoForm(request.POST)
        if form.is_valid():
            nuevo = form.save()
            # Si quieres ir al detalle después de crear:
            # return redirect('detalle_equipo', pk=nuevo.pk)
            return redirect("lista_equipos")
    return render(request, "lista_equipos.html", {"equipos": equipos, "form": form})


# DETALLE
def detalle_equipo(request, pk):
    equipo = get_object_or_404(Equipo, pk=pk)
    return render(request, "detalle_equipo.html", {"equipo": equipo})


# CREAR
def crear_equipo(request):
    if request.method == "POST":
        form = EquipoForm(request.POST)
        if form.is_valid():
            equipo = form.save()
            return redirect("equipos:detalle_equipo", pk=equipo.pk)
    else:
        form = EquipoForm()
    return render(
        request,
        "formulario_equipo.html",
        {"form": form, "titulo": "Registrar nuevo equipo"},
    )


# EDITAR
def editar_equipo(request, pk):
    equipo = get_object_or_404(Equipo, pk=pk)
    if request.method == "POST":
        form = EquipoForm(request.POST, instance=equipo)
        if form.is_valid():
            equipo = form.save()  # <- asegúrate de tener la instancia
            return redirect(
                "equipos:detalle_equipo", pk=equipo.pk
            )  # <- usa pk, no .id si tu URL usa pk
    else:
        form = EquipoForm(instance=equipo)
    return render(
        request,
        "formulario_equipo.html",
        {"form": form, "titulo": "Editar equipo"},
    )


# ELIMINAR
def eliminar_equipo(request, pk):
    equipo = get_object_or_404(Equipo, pk=pk)
    equipo.delete()
    return redirect("equipos:lista_equipos")
