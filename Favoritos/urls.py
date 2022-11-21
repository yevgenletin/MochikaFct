
from django.urls import path

from Favoritos import views
from django.conf import settings
from django.conf.urls.static import static
from .views import CreateFavoritos
urlpatterns = [
    path('', views.favoritos, name="favoritos"),
    path('create-favoritos/', views.CreateFavoritos.as_view(), name="create-favoritos"),
    path('update-favoritos/', views.UpdateFavoritos.as_view(), name="update-favoritos"),

    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)