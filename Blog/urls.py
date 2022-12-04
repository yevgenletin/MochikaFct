
from django.urls import path

from Blog import views, admin
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #path('', views.lista, name="lista"),
    path('', views.recetas, name="recetas"),
    path('receta/<int:post_id>/', views.receta, name="receta"),
    path('comentario/<int:post_id>/', views.comentario, name="comentario"),
    path('categoria/<int:categoria_id>/', views.categoria, name="categoria"),
]
   


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)