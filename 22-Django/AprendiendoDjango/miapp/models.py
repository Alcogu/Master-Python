from django.db import models

# pequeñas clases que generan objetos para trabajar en el proyecto
#Modelo es una tabla de la base de datos

#Se define modelo
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    public = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)#Guarda fecha de creación
    updated_at = models.DateTimeField(auto_now=True)#Guarda fecha de edición

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    created_at = models.DateTimeField()#se guarda manualmente