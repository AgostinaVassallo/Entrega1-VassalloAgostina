from django.urls import path
from appbts import views
from appbts.views import *




urlpatterns = [
    path('inicio/', inicio, name='inicio'),
    path('bts/', bts, name='bts'),
    path('coreasur/', coreasur, name='coreasur'),
    path('army/', army, name='army'),
    path('btsFormulario/', btsFormulario, name='btsFormulario'),
    path('coreaFormulario/', coreaFormulario, name='coreaFormulario'),
    path('armyFormulario/', armyFormulario, name='armyFormulario'),
    path('busquedaBts/', busquedaBts, name='busquedaBts'),
    path('buscar/', buscar, name='buscar'),
]