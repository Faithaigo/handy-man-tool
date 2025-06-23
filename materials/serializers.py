from rest_framework import serializers

from materials.models import Material


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = ["id","name","created_at","updated_at","created_by","updated_by"]
        read_only_fields = ["id","created_at","updated_at"]