from rest_framework import serializers
from . import models


class TodoSerializer(serializers.ModelSerializer):

    class Meta:
        fields = (
            'id',
            'title',
            'created_at',
            'duedate',
            'completed',
        )
        model = models.Todo
