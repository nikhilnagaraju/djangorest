from rest_framework import generics, filters
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView

from . import models
from . import serializers


class ListTodo(ListCreateAPIView):
    queryset = models.Todo.objects.all()
    serializer_class = serializers.TodoItemSerializer


class DetailTodo(RetrieveUpdateDestroyAPIView):
    queryset = models.Todo.objects.all()
    serializer_class = serializers.TodoItemSerializer