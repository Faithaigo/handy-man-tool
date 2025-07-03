from rest_framework import serializers

from tasks.models import Task, TaskMaterial, TaskTool
from materials.models import Material
from tools.models import Tool
from django.db import transaction


class TaskMaterialSerializer(serializers.ModelSerializer):
    material_id = serializers.PrimaryKeyRelatedField(queryset=Material.objects.all(), source='material')

    material_name = serializers.CharField(source='material.name', read_only=True)

    class Meta:
        model = TaskMaterial
        fields = ['material_id', 'material_name', 'quantity']


class TaskToolSerializer(serializers.ModelSerializer):
    tool_id = serializers.PrimaryKeyRelatedField(queryset=Tool.objects.all(),
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

    def update(self, instance, validated_data):
        materials_data = validated_data.pop('taskmaterial_set',[])
        tools_data = validated_data.pop('tasktool_set',[])

        for attr, val in validated_data.items():
            setattr(instance, attr, val)
        instance.save()

        #materials
        existing_materials = {}
        incoming_materials = {}

        for e_mat in instance.taskmaterial_set.all():
            existing_materials[e_mat.material.id] = e_mat

        for i_mat in materials_data:
            incoming_materials[i_mat['material'].id] = i_mat

        for mat_id in set(existing_materials) - set(incoming_materials): #find what is in existing_materials that is not in incoming materials
            existing_materials[mat_id].delete()

        for mat_id, mat_data in incoming_materials.items():
            if mat_id in existing_materials:
                task_mat = existing_materials[mat_id]
                if task_mat.quantity != mat_data['quantity']:
                    task_mat.quantity = mat_data['quantity']
                    task_mat.save()
            else:
                TaskMaterial.objects.create(task=instance, **mat_data)

        #tools
        existing_tools = {}
        incoming_tools = {}

        for e_tool in instance.tasktool_set.all():
            existing_tools[e_tool.tool.id] = e_tool

        for i_tool in tools_data:
            incoming_tools[i_tool['tool'].id] = i_tool

        #Remove tools not in the update data
        for tool_id in set(existing_tools) - set(incoming_tools):
            existing_tools[tool_id].delete()

        #update existing tools or add new tools
        for tool_id, tool_data in incoming_tools.items():
            if tool_id in existing_tools:
                task_tool = existing_tools[tool_id]
                if task_tool.quantity != tool_data['quantity']:
                    task_tool.quantity = tool_data['quantity']
                    task_tool.save()
            else:
                TaskTool.objects.create(task=instance, **tool_data)

        return instance