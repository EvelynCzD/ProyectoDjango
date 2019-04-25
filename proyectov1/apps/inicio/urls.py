from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from .views import inicio, lista_jugador, equipos, ListaJugador, ListaEquipos


urlpatterns = [
    path('',LoginView.as_view(template_name='base.html'), name="login"),
    path('cerrar/', LogoutView.as_view(), name= "logout"),
    path('inicio', inicio, name = "inicio"), 
    path('jugadores', lista_jugador, name="lista_jugador"),
    path('equipos', equipos, name="equipos"),
    path('api/listajugador/', ListaJugador.as_view(), name="ListaJugador"),
    path('api/equipos/', ListaEquipos.as_view(), name="ListaEquipos"),
    path('catalogos/', include('apps.catalogos.urls'),),
]
