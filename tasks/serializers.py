from rest_framework import serializers
from .models import Task

# class TaskSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Task
#         fields = "__all__"
#         read_only_fields = ["user", "created_at", "modified_at"]


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"
        read_only_fields = ["user", "created_at", "modified_at"]

    # field-level validation
    def validate_title(self, value):
        if len(value.strip()) < 3:
            raise serializers.ValidationError("Title must be at least 3 characters long.")
        return value

    def validate_description(self, value):
        if not value.strip():
            raise serializers.ValidationError("Description cannot be empty.")
        return value

    # object-level validation
    def validate(self, data):
        if data.get("attachment") and data["attachment"].size > 5 * 1024 * 1024:  # 5MB
            raise serializers.ValidationError({"attachment": "File size must be less than 5MB."})
        return data
