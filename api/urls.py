from django.urls import path, include
from rest_framework import routers  # Importación correcta
from api import views

router = routers.DefaultRouter()  # Uso correcto de DefaultRouter
router.register(r'peliculas', views.PeliculaViewSet)

urlpatterns = [
    path('', include(router.urls))  # Incluir las URLs del router
]
