from django.db import models

# pequeñas clases que generan objetos para trabajar en el proyecto
#Modelo es una tabla de la base de datos

#Se define modelo
class Article(models.Model):
    title = models.CharField(max_length=150, verbose_name = "Titulo")
    content = models.TextField(verbose_name = "Contenido")
    image = models.ImageField(default='null', verbose_name = "Miniatura")
    public = models.BooleanField(verbose_name = "¿Publicado?")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name = "Creado")#Guarda fecha de creación
    updated_at = models.DateTimeField(auto_now=True, verbose_name = "Editado")#Guarda fecha de edición

    class Meta:
        verbose_name = "Articulo"
        verbose_name_plural = "Articulos"
        ordering = ['id']

    def __str__(self):

        if self.public:
            public = "(publicado)"
        else:
            public = "(privado)"
            
        return f"{self.title} {public}"

class Category(models.Model):
    name = models.CharField(max_length=110)
    description = models.CharField(max_length=250)
    created_at = models.DateTimeField()#se guarda manualmente

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"