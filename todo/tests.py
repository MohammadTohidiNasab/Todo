from django.test import TestCase
from .models import Todo
from model_bakery import baker

"""baker fill out inputs you dont need to test"""
# Create your tests here.


class TestTodoModel(TestCase):
    def test_model_str(self):
        new_todo = baker.make(Todo, title="todo")
        self.assertEqual(str(new_todo), "todo")
