
from django.urls import path
from todos.views import TodoListListView, TodoListDetailView


urlpatterns = [
    path("", TodoListListView.as_view(), name="list_todos"),
    path("<int:pk>/", TodoListDetailView.as_view(), name="show_todolist")
]
