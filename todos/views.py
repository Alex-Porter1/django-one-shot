from django.shortcuts import render
from todos.models import TodoItem, TodoList
from django.views.generic.detail import DetailView
# Create your views here.
from django.views.generic.list import ListView
from django.urls import reverse_lazy


class TodoListListView(ListView):
    model = TodoList
    template_name = "todos/list.html"
    context_object_name = "todolist"


class TodoListDetailView(DetailView):
    model = TodoList
    template_name = "todos/detail.html"
