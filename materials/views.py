
from rest_framework import viewsets

from materials.models import Material
from materials.serializers import MaterialSerializer


class MaterialViewSet(viewsets.ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
