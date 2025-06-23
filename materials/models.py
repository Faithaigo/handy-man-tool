from django.contrib.auth.models import User
from django.db import models


class Material(models.Model):
    name = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='materials_updated_by')
    updated_at = models.DateTimeField(auto_now=True)
