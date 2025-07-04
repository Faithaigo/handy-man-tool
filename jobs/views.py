from rest_framework import viewsets
from .models import Client
from .serializers import ClientsSerializer



class ClientsViewSets(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientsSerializer