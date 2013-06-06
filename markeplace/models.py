from django.db import models


class Categoria(models.Model):
    nombre = models.CharField(max_length= 20)

    def __unicode__(self):
        return selt.nombre

class Persona(models.Model):
    nombre = models.CharField(max_length = 20)
    apellido = models.CharField(max_length = 20)
    correo = models.EmailField()
    telefono = models.CharField(max_length = 10)
    direccion = models.CharField(max_length = 20, null= True)
    foto = models.ImageField(upload_to='fotos', verbose_name='Foto')
    usuario = models.CharField(max_length = 20)
    password = models.CharField(max_length = 20)
    fecha_registro = models.DateTimeField(auto_now = True)

    def __unicode__(self):
        return self.nombre +''+self.apellido +''+ self.correo +''+ self.telefono +''+ self.direccion +''+ self.foto
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

class Contactenos(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length = 20)
    asunto = models.CharField(max_length = 30)
    correo = models.EmailField()
    descripcion = models.CharField(max_length = 300)

    def __unicode__(self):
        return self.nombre +''+ self.apellido +''+ self.asunto +''+ self.correo +''+ self.descripcion

class Articulo(models.Model):
    nombre = models.CharField(max_length = 20)
    precio = models.CharField(max_length = 8)
    categoria = models.ForeignKey(Categoria)
    imagen = models.ImageField(upload_to='imagenes', verbose_name='Imagen')
    publicado = models.DateTimeField(auto_now=True)
    descripcion = models.CharField(max_length = 300)
    recomendar = models.ForeignKey(Recomendados, null= True)
    destacar = models.ForeignKey(Destacados, null= True)

    def __unicode__(self):
        return self.nombre +''+ self.precio +''+ self.publicado +''+ self.descripcion +''+ self.recomendar +''+ self.destacar
