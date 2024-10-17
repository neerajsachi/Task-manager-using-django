from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    title = serializers.CharField(
        error_messages={
            'blank': 'Title cannot be empty.',
            'required': 'Title is required.'
        }
    )
    description = serializers.CharField(
        error_messages={
            'blank': 'Description cannot be empty.',
            'required': 'Description is required.'
        }
    )

    completed = serializers.BooleanField(
        error_messages={
            'required': 'Completed is required'
        }
    )

    class Meta:
        model = Task
        fields = ['title', 'description', 'created_at', 'completed']
