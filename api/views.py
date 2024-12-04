from rest_framework import viewsets
from .models import Pelicula
from .serializer import PeliculaSerializer
# Create your views here.
class PeliculaViewSet(viewsets.ModelViewSet):
    queryset=Pelicula.objects.all() # pylint: disable=no-member
    serializer_class=PeliculaSerializer