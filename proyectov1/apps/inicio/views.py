from django.shortcuts import render
from .models import equipo
from .models import jugador
from .serializers import EquipoSerializers, JugadorSerializers
from rest_framework.views import APIView
from rest_framework.response import Response 

# Create your views here.

def inicio(request):
	equipos = equipo.objects.all()
	nombre = "nombre nombre del usuario"
	nombres = ["Luis", "Pepes", "Andres", "Juan", "Jose"]
	return render(request, "inicio/index.html", {"equipos":equipos})

	
def lista_jugador(request):

	jugadores = jugador.objects.all()
	return render(request, "inicio/lista_jugadores.html", {"jugadores":jugadores})

def equipos(request):
	equipos = equipo.objects.all()
	return render(request, "inicio/equipos.html", {"equipos":equipos})


	#equipo.objets.get unicamente si se quiere obtener un dato
	#equipo.objects.filter unicamente regresa un arreglo de un conjunto de la tabla  

class ListaJugador(APIView):
	def get(self, request):
		jugadores = jugador.objects.all()
		jugadores_json = JugadorSerializers(jugadores, many= True)
		return Response(jugadores_json.data)



class ListaEquipos(APIView):
	def get(self, request):
		equipos = equipo.objects.all()
		equipos_json = EquipoSerializers(equipos, many=True)
		return Response(equipos_json.data)

				