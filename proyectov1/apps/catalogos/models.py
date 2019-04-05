from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Entidad(models.Model):
	clave = models.CharField(max_length=10, blank=True, null=True)
	nombre= models.CharField(max_length=10, blank=True, null=True)

class Municipio(models.Model):
	entidad = models.ForeignKey(Entidad, on_delete=models.CASCADE)
	nombre = models.CharField(max_length=10, blank=True, null=True)

class Disciplina(models.Model):
	nombre = models.CharField(max_length=100)

class Modalidad(models.Model):
	disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE,related_name='modalidad_disciplina')
	descripcion= models.CharField(max_length=100, blank=True, null=True)

class Torneo(models.Model):
	nombre = models.CharField(max_length=10, blank=True, null=True)
	fecha_inicio= models.DateField(blank=True, null=True)
	fecha_final= models.DateField(blank=True, null=True)
	municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)
	ciudad = models.CharField(max_length=100,blank=True,null=True)
	disciplina= models.ForeignKey(Disciplina, on_delete= models.CASCADE)
	convocatoria = models.FileField(upload_to="pdfconvocatoria",blank=True,null=True)


class User(AbstractUser):
	nacimiento=models.DateField(blank=True, null=True)
	telefono=models.IntegerField(max_length=15, blank=True, null=True)
	tiposangre=models.CharField(max_length=10, blank=True, null=True)
	fotografia = models.ImageField(upload_to="")

	
class Arbitro(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='usuario_arbitro')
	disciplina = models.ForeignKey(Disciplina,on_delete=models.CASCADE,related_name='disciplina_arbitro')
	modalidad= models.ForeignKey(Modalidad, on_delete=models.CASCADE)

class Director(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='usuario_director')

class Equipo(models.Model):
	nombre = models.CharField(max_length=30, blank=True, null=True)
	director=models.ForeignKey(Director, on_delete=models.CASCADE)
	creacion= models.DateField(blank=True, null=True)
	torneo=models.ForeignKey(Torneo, on_delete=models.CASCADE)
	logo = models.ImageField(upload_to="img_equipo",blank=True,null=True)

class Instalaciones(models.Model):
	ubicacion= models.CharField(max_length=15, blank=True, null=True)
	lugar= models.CharField(max_length=15, blank=True, null=True)
	imagen = models.ImageField(upload_to="imginstalacion",blank=True,null=True)



class Jugador(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='usuario_jugador')
	equipo= models.ForeignKey(Equipo, on_delete=models.CASCADE)
	alias=models.CharField(max_length=15, blank=True, null=True)
	posicion=models.CharField(max_length=10, blank=True, null=True)
	dorsal=models.IntegerField(max_length=3, blank=True, null=True)


