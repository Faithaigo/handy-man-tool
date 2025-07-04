from django.contrib.auth.models import User
from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=100, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Job(models.Model):
    name = models.CharField(max_length=100)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="job_updated_by")
    updated_at = models.DateTimeField(auto_now=True)