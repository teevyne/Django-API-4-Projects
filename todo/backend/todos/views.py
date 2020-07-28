from django.shortcuts import render
from rest_framework import generics
from .serializers import TodoSerializer
from .models import Todo

# Create your views here.

# class to display all todo's
class ListTodo(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

# class to display a single todo item/instance
class DetailTodo(generics.RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer