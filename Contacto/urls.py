
from django.urls import path

from Contacto import views, admin
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.contacto, name="contacto"),
    path('events', views.contacto, name="contacto"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)