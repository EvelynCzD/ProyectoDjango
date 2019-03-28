from rest_framework import serializers
from .models import equipo, jugador

class EquipoSerializers(serializers.ModelSerializer):
	class Meta:
		model = equipo
		fields = ('__all__')



class JugadorSerializers(serializers.ModelSerializer):
	equipo = EquipoSerializers(read_only = True) #Es un campo del modelo Equipo 
	class Meta:
		model = jugador
		fields = ('__all__')