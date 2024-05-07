from django.shortcuts import get_object_or_404, redirect
from django.views import generic
from .models import Todo
from .serializers import ToDoSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

'''
main page show all tasks
'''
class IndexView(generic.ListView):
    template_name = "todos/index.html"
    context_object_name = "todo_list"

    def get_queryset(self):
        """Return all the latest todos."""
        return Todo.objects.order_by("-created_at")


def add(request):
    title = request.POST["title"]
    Todo.objects.create(title=title)

    return redirect("todos:index")


def delete(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    todo.delete()

    return redirect("todos:index")


def update(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    isCompleted = request.POST.get("isCompleted", False)
    if isCompleted == "on":
        isCompleted = True

    todo.isCompleted = isCompleted

    todo.save()
    return redirect("todos:index")


# api
class ListTodo(generics.ListAPIView):
    """
    a list of tasks
    """

    queryset = Todo.objects.all()
    serializer_class = ToDoSerializer
    search_fields = ["title"]
    ordering_fields = ["created_at"]


class Cred(generics.RetrieveUpdateDestroyAPIView):
    """
    cred (read create edite delete tasks)
    """

    queryset = Todo.objects.all()
    serializer_class = ToDoSerializer
    permission_classes = [IsAuthenticated]
