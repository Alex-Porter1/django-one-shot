from django.shortcuts import render
from todos.models import TodoItem, TodoList

# Create your views here.
from django.views.generic.list import ListView


class TodoListListView(ListView):
    model = TodoList
    template_name = "todos/list.html"
    context_object_name = "todolist"
