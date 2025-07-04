from rest_framework import viewsets
from .models import Client, Job
from .serializers import ClientsSerializer, JobSerializer



class ClientsViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientsSerializer

class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer