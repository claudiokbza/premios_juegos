from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True, null=True)
    imagen = models.URLField(blank=True, null=True) 

    def __str__(self):
        return self.nombre    

class Juego(models.Model):
    titulo = models.CharField(max_length=200)
    desarrolladora = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_lanzamiento = models.DateField()
    imagen = models.URLField(blank=True) 

    def __str__(self):
        return self.titulo

class Nominacion(models.Model):
    juego = models.ForeignKey(Juego, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    

    def __str__(self):
        return f"{self.juego.titulo} nominado en {self.categoria.nombre}"
    
