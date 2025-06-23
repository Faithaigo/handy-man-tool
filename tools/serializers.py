from rest_framework import serializers

from tools.models import Tool


class ToolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tool
        fields = ["id","name","created_at","updated_at","created_by","updated_by"]
        read_only_fields = ["id","created_at","updated_at"]