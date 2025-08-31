from django.urls import path
from . import views

urlpatterns = [
    path('', views.portada_categorias, name='portada_categorias'),
    path('categoria/<int:categoria_id>/', views.juegos_nominados, name='juegos_nominados'),
    path('juego/<int:juego_id>/', views.detalle_juego, name='detalle_juego'),
]