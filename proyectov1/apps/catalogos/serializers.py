from rest_framework import serializers
from .models import Entidad, Municipio, Disciplina,Modalidad, Torneo,User, Director, Arbitro, Equipo, Jugador, Instalaciones

class EntidadSerializers(serializers.ModelSerializer):
	class Meta:
		model = Entidad
		fields = ('__all__')


class MunicipioSerializers(serializers.ModelSerializer):
	entidad = EntidadSerializers(read_only=True)

	class Meta:
		model = Municipio
		fields = ('__all__')	

class DisciplinaSerializers(serializers.ModelSerializer):
	class Meta:
		model = Disciplina
		fields = ('__all__')

class ModalidadSerializers(serializers.ModelSerializer):
	disciplina = DisciplinaSerializers(read_only=True)
	class Meta:
		model = Modalidad
		fields = ('__all__')

class TorneoSerializers(serializers.ModelSerializer):
	class Meta:
		model = Torneo
		fields = ('__all__')



class UserSerializers(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('__all__')

class ArbitroSerializers(serializers.ModelSerializer):
	user = UserSerializers(read_only=True)
	disciplina = DisciplinaSerializers(read_only=True)
	modalidad = ModalidadSerializers(read_only=True)

	class Meta:
		model = Arbitro
		fields = ('__all__')

class DirectorSerializers(serializers.ModelSerializer):
	user = UserSerializers(read_only=True)


class EquipoSerializers(serializers.ModelSerializer):
	director = DirectorSerializers(read_only=True)
	torneo = TorneoSerializers(read_only=True)
	class Meta:
		model = Equipo
		fields = ('__all__')



class JugadorSerializers(serializers.ModelSerializer):
	Equipo = EquipoSerializers(read_only = True) #Es un campo del modelo Equipo 
	class Meta:
		model = Jugador
		fields = ('__all__')


class InstalacionesSerializers(serializers.ModelSerializer):
	class Meta:
		model = Instalaciones
		fields = ('__all__')
