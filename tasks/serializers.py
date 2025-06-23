from rest_framework import serializers

from tasks.models import Task, TaskMaterial, TaskTool
from materials.models import Material
from tools.models import Tool
from django.db import transaction


class TaskMaterialSerializer(serializers.ModelSerializer):
    material_id = serializers.PrimaryKeyRelatedField(queryset=Material.objects.all(), write_only=True, source='material')

    material_name = serializers.CharField(source='material.name', read_only=True)

    class Meta:
        model = TaskMaterial
        fields = ['material_id', 'material_name', 'quantity']


class TaskToolSerializer(serializers.ModelSerializer):
    tool_id = serializers.PrimaryKeyRelatedField(queryset=Tool.objects.all(), write_only=True,
                                                     source='tool')

    tool_name = serializers.CharField(source='tool.name', read_only=True)

    class Meta:
        model = TaskTool
        fields = ['tool_id', 'tool_name', 'quantity']


class TaskSerializer(serializers.ModelSerializer):
    tools = TaskToolSerializer(many=True, source="tasktool_set")
    materials = TaskMaterialSerializer(many=True, source="taskmaterial_set")

    class Meta:
        model = Task
        fields = ['id', 'name', 'materials', 'tools', 'job', 'created_at', 'created_by', 'updated_at', 'updated_by']
        read_only_fields = ['created_at', 'updated_at', 'updated_by',"job"]

    @transaction.atomic
    def create(self, validated_data):
        materials_data = validated_data.pop('taskmaterial_set')
        tools_data = validated_data.pop('tasktool_set')

        task = Task.objects.create(**validated_data)

        for material_data in materials_data:
            TaskMaterial.objects.create(task=task, **material_data)

        for tool_data in tools_data:
            TaskTool.objects.create(task=task, **tool_data)

        return task