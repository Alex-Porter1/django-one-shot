from django.shortcuts import render
from todos.models import TodoItem, TodoList
from django.views.generic.detail import DetailView
# Create your views here.
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView


class TodoListListView(ListView):
    model = TodoList
    template_name = "todos/list.html"
    context_object_name = "todolist"


class TodoListDetailView(DetailView):
    model = TodoList
    template_name = "todos/detail.html"


class TodoListCreateView(CreateView):
    model = TodoList
    template_name = "todos/create.html"
    fields = ["name"]

    def get_success_url(self):
        return reverse_lazy("show_todolist", args=[self.object.id])


class TodoListUpdateView(UpdateView):
    model = TodoList
    template_name = "todos/update.html"
    fields = ["name"]

    def get_success_url(self):
        return reverse_lazy("show_todolist", args=[self.object.id])


class TodoListDeleteView(DeleteView):
    model = TodoList
    template_name = "todos/delete.html"
    success_url = reverse_lazy("list_todos")