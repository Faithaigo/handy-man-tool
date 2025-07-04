from rest_framework import serializers
from tasks.models import Task
from .models import Job, Client


class ClientsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = ["id", "name","address","contact", "created_by", "created_at"]
        read_only_fields =["id","created_at"]