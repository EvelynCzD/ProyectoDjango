from django.db import models

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
	disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
	descripcion= models.CharField(max_length=100, blank=True, null=True)

class Torneo(models.Model):
	nombre = models.CharField(max_length=10, blank=True, null=True)
	fecha_inicio= models.DateField(blank=True, null=True)
	fecha_final= models.DateField(blank=True, null=True)
	municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)
	disciplina= models.ForeignKey(Disciplina, on_delete= models.CASCADE)
	arbitro= models.ForeignKey(Arbitro, on_delete=models.CASCADE)

class Director(models.Model):
	nombre = models.CharField(max_length=30, blank=True, null=True)
	telefono= models.CharField(max_length=15, blank=True, null=True)
	direccion= models.CharField(max_length=30, blank=True, null=True)
	equipo= models.ForeignKey(Equipo, on_delete=models.CASCADE)
	correo= models.CharField(max_length=30, blank=True, null=True)

class Equipo(models.Model):
	nombre = models.CharField(max_length=30, blank=True, null=True)
	director=models.ForeignKey(Director, on_delete=models.CASCADE)
	creacion= models.DateField(blank=True, null=True)
	municipio=models.ForeignKey(Municipio, on_delete=models.CASCADE)
	torneo=models.ForeignKey(Torneo, on_delete=models.CASCADE)

class Jugador(models.Model):
	nombre = models.CharField(max_length=15, blank=True, null=True)
	apellido= models.CharField(max_length=15, blank=True, null=True)
	equipo= models.ForeignKey(Equipo, on_delete=models.CASCADE)
	alias=models.CharField(max_length=15, blank=True, null=True)
	posicion=models.CharField(max_length=10, blank=True, null=True)
	dorsal=models.IntegerField(max_length=3, blank=True, null=True)
	nacimiento=models.DateField(blank=True, null=True)
	telefono=models.IntegerField(max_length=15, blank=True, null=True)
	tiposangre=models.CharField(max_length=10, blank=True, null=True)

class Arbitro(models.Model):
	nombre= models.CharField(max_length=15, blank=True, null=True)
	apellido= models.CharField(max_length=15, blank=True, null=True)
	edad= models.IntegerField(max_length=3, blank=True, null=True)
	modalidad= models.ForeignKey(Modalidad, on_delete=models.CASCADE)

class Instalaciones(models.Model):
	ubicacion= models.CharField(max_length=15, blank=True, null=True)
	lugar= models.CharField(max_length=15, blank=True, null=True)
