from django.contrib import admin
from .models import Entidad, Municipio, Torneo, Equipo, Jugador, Director, Arbitro, User, Instalaciones, Disciplina, Modalidad

admin.site.Register(Entidad) 
admin.site.Register(Municipio)
admin.site.Register(Torneo)
admin.site.Register(Equipo)
admin.site.Register(Jugador)
admin.site.Register(Director)
admin.site.Register(Arbitro)
admin.site.Register(User)
admin.site.Register(Instalaciones)
admin.site.Register(Disciplina)
admin.site.Register(Modalidad)

