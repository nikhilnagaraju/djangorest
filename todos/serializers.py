from rest_framework import serializers
from . import models


class TodoSerializer(serializers.ModelSerializer):

    class Meta:
        fields = (
            'id',
            'title',
            'created_at',
            'duedate',
            'is_finished',
        )
        model = models.Todo
