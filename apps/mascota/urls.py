from django.urls import path, include
from apps.mascota.views import index, mascota_view, mascota_list, mascota_edit, mascota_delete, \
	MascotaList, MascotaCreate

urlpatterns = [
    path('', index, name='index'),
    path('nuevo/', MascotaCreate.as_view(), name='mascota_crear'),
    path('listar/', MascotaList.as_view(), name='mascota_listar'),
    path('editar/<int:id_mascota>/', mascota_edit, name='mascota_editar'),
    path('eliminar/<int:id_mascota>/', mascota_delete, name='mascota_eliminar'),
]