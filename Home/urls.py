
from django.urls import path

from Home import views, admin
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('recetas/', views.recetas, name="recetas"),
    path('restaurantes/', views.restaurantes, name="restaurantes"),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)