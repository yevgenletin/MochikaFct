
from django.urls import path

from Autentificacion import views, admin
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.autentificacion, name="autentificacion"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)