from rest_framework import viewsets
from tasks.serializers import TaskSerializer
from tasks.models import Task

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer




