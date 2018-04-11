from rest_framework import serializers
from todos.models import Todo #, TodoList

''' Script Used to convert python objects to json objects.'''


class TodoItemSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id',
                  'title',
                  'created_at',
                  'duedate',
                  'completed',
                  # 'todolist',
                  )
        model = Todo


# class TodolistSerializer(serializers.ModelSerializer):
#
#     items = TodoItemSerializer(many=True, read_only=True)
#
#     class Meta:
#         fields = ('id',
#                   'title',
#                   'created_at',
#                   'duedate',
#                   'completed',
#                   'items'
#                   )
#         model = TodoList