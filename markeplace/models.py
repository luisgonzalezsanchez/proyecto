from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    nombre = models.CharField(max_length= 20)

    def __unicode__(self):
        return self.nombre

class Persona(User):
    telefono = models.CharField(max_length = 10)
    direccion = models.CharField(max_length = 20, null= True)
    foto = models.ImageField(upload_to='fotos', verbose_name='Foto')
    fecha_registro = models.DateTimeField('fecha de publicacion')

    def __unicode__(self):
        return self.nombre +''+self.apellido +''+ self.correo +''+ self.telefono +''+ self.direccion +''+ self.foto.name
        +''+ self.usuario +''+ self.password +''+ self.fecha_registro

class Recomendados(models.Model):
    RECOMENDAR = ((u'S', u'Si'), (u'N', u'No'))
    recomendar = models.CharField(max_length=2, choices=RECOMENDAR)

    def __unicode__(self):
        return self.recomendar

class Destacados(models.Model):
    DESTACAR = ((u'S', u'Si'), (u'N', u'No'))
    destacar = models.CharField(max_length=2, choices=DESTACAR)
    
    def __unicode__(self):
        return self.destacar

class Articulo(models.Model):
    nombre = models.CharField(max_length = 20)
    precio = models.CharField(max_length = 8)
    categoria = models.ForeignKey(Categoria)
    imagen = models.ImageField('imagen', upload_to='imagenes/')
    publicado = models.DateTimeField('publicado')
    descripcion = models.CharField(max_length = 300)
    recomendar = models.ForeignKey(Recomendados, null= True)
    destacar = models.ForeignKey(Destacados, null= True)

    def __unicode__(self):
        return self.nombre +''+ self.precio +''+ self.imagen.name +''+ self.descripcion
