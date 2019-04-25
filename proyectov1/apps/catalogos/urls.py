from django.urls import path
from .views import ListaMunicipio

urlpatterns = [
	path('api/lista/municipio/', ListaMunicipio.as_view(), name="ListaMunicipio")
]