
from django.urls import path

from Autentificacion import views, admin
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from .views import Vregistro, cerrar_sesion, login


urlpatterns = [
    path('', Vregistro.as_view(), name="autentificacion"),
    path('cerrar_sesion', cerrar_sesion, name="cerrar_sesion"),
    path('login', login, name="login"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)