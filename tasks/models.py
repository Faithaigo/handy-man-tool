from django.contrib.auth.models import User
from django.db import models

from jobs.models import Job
from materials.models import Material
from tools.models import Tool


class Task(models.Model):
    name = models.CharField(max_length=100)
    materials = models.ManyToManyField(Material, through='TaskMaterial')
    tools = models.ManyToManyField(Tool, through='TaskTool')
    job = models.ForeignKey(Job, related_name="tasks", on_delete=models.CASCADE, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='tasks_updated_by')
    updated_at = models.DateTimeField(auto_now=True)


class TaskMaterial(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['task', 'material'], name='unique_task_material'
            )
        ]

class TaskTool(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    tool = models.ForeignKey(Tool, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['task', 'tool'], name='unique_task_tool'
            )
        ]
