from django.urls import path

from ListadoProductos import views, admin
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.InfoListView.as_view(), name="lista"),
    path('<int:alimento_id>/', views.alimento, name="alimento")
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)