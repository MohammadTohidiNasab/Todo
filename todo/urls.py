from django.urls import path
from .views import ListTodo, Cred, IndexView, delete, update, add


app_name = "todos"
urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("<int:todo_id>/delete", delete, name="delete"),
    path("<int:todo_id>/update", update, name="update"),
    path("add/", add, name="add"),
    # api urls
    path("api/", ListTodo.as_view()),
    path("api/<int:pk>/", Cred.as_view(), name="cred"),
]
