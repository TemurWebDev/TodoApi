import unittest
from django.test import TestCase
from django.utils import timezone
from .models import Task

class TaskModelTest(TestCase):
    def setUp(self):
        Task.objects.create(
            start_time=timezone.now(),
            end_time=timezone.now(),
            title='Test task',
            description='This is a test task',
            status='todo'
        )

    def test_task_title(self):
        task = Task.objects.get(title='Test task')
        self.assertEqual(task.title, 'Test task')

    def test_task_description(self):
        task = Task.objects.get(title='Test task')
        self.assertEqual(task.description, 'This is a test task')

    def test_task_status(self):
        task = Task.objects.get(title='Test task')
        self.assertEqual(task.status, 'todo')

    def test_task_str_method(self):
        task = Task.objects.get(title='Test task')
        self.assertEqual(str(task), 'Test task')

if __name__ == '__main__':
    unittest.main()
