from rest_framework import serializers
from tasks.models import Task
from .models import Job, Client
from django.db import transaction


class ClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ["id", "name", "address", "contact", "created_by", "created_at"]
        read_only_fields = ["id", "created_at"]


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["id", "name"]
        read_only_fields = ["name"]


class JobSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True)

    class Meta:
        model = Job
        fields = ["id", "name", "client", "tasks", "created_by", "created_at", "updated_by", "updated_at"]
        read_only_fields = ["id", "created_by", "created_at", "updated_by", "updated_at"]

    @transaction.atomic
    def create(self, validated_data):
        tasks_data = validated_data.pop("tasks", [])
        print(tasks_data)

        job = Job.objects.create(**validated_data)

        for task_data in tasks_data:
            print('task_data', task_data["id"])
            task = Task.objects.get(id=task_data["id"])
            task.job = job
            task.save()

        return job
