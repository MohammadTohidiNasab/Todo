from rest_framework import serializers
from .models import Todo

class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'title', 'Description', 'created_at', 'isCompleted')
