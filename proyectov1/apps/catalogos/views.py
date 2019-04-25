from django.shortcuts import render
from .models import Entidad, Municipio, Disciplina, Modalidad, Torneo,User, Director, Arbitro, Equipo, Jugador, Instalaciones
from .serializers import EntidadSerializers, MunicipioSerializers, DisciplinaSerializers, ModalidadSerializers, TorneoSerializers, UserSerializers, DirectorSerializers, ArbitroSerializers, EquipoSerializers, JugadorSerializers, InstalacionesSerializers
from rest_framework.views import APIView
from rest_framework.response import Response


class ListaMunicipio(APIView):
	def get(self, request):
		clave = request.GET['idmunicipio']
		if clave == '0':
			municipios = Municipio.objects.all()
		else:
			municipios= Municipio.objects.filter(id = clave)
		municipios_json = MunicipioSerializers(municipios, many= True)
		return Response(municipios_json.data) 

class ListaModalidad(APIView):
	def get(self, request):
		disciplina = request.GET['iddisciplina']
		if disciplina == '0':
			disciplinas = Disciplina.objects.all()
		else:
			disciplinas= Disciplina.objects.filter(id = disciplina)
			disciplinas_json = DisciplinaSerializers(disciplinas, many = True)


# Create your views here.
