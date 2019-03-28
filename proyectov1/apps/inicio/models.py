from django.db import models

#Formulario para creacion de tablas(Modelos)

class equipo(models.Model):
	nombre=models.CharField(max_length=100, blank=True, null=True)
	responsable=models.CharField(max_length= 100, blank=True)
	creacion=models.DateField(blank=True)
	def __str__(self): 
		return self.nombre




class jugador(models.Model):

	ESTADO_JUGADOR = (
	('A', 'ACTIVO'),
	('L', 'LESIONADO'),
	('S', 'SUSPENDIDO'),
	)

	equipo = models.ForeignKey("equipo", on_delete=models.CASCADE)
	nombre = models.CharField(max_length=250, blank=True, null=True)
	alias = models.CharField(max_length=100, blank=True, null=True)
	posicion = models.CharField(max_length=100, blank=True, null=True)
	nacimiento = models.DateField(blank=True)
	dorsal = models.CharField(max_length=3, blank=True, null=True)
	fotografia=models.ImageField(upload_to="img-jugador", blank=True, null=True)
	estatus = models.CharField(max_length=1, choices= ESTADO_JUGADOR)

	def __str__(self):
		return self.nombre
# Create your models here.

