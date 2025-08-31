from django.shortcuts import render

from django.shortcuts import render, get_object_or_404
from .models import Categoria, Juego, Nominacion

def portada_categorias(request):
    categorias = Categoria.objects.all()
    context = {'categorias': categorias}
    return render(request, 'juegos/portada_categorias.html', context)

def juegos_nominados(request, categoria_id):
    categoria = get_object_or_404(Categoria, pk=categoria_id)
    nominaciones = Nominacion.objects.filter(categoria=categoria)
    context = {
        'categoria': categoria,
        'nominaciones': nominaciones
    }
    return render(request, 'juegos/juegos_nominados.html', context)

def detalle_juego(request, juego_id):
    juego = get_object_or_404(Juego, pk=juego_id)
    nominaciones = Nominacion.objects.filter(juego=juego)
    context = {
        'juego': juego,
        'nominaciones': nominaciones
    }
    return render(request, 'juegos/detalle_juego.html', context)