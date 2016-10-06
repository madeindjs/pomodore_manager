from django.test import TestCase, Client
from django.urls import reverse

from .models import Task

class TaskMethodTests(TestCase):

    def test_should_create_a_task_whithout_parent(self):
        new_task = Task(parent=None, name="name", description="description")
        new_task.save()

        self.assertIsNotNone(new_task.id)



    def test_should_return_parent_task(self):
        parent_task = Task(parent=None, name="name", description="description")
        parent_task.save()
        child_task = Task(parent=parent_task, name="name", description="description")
        child_task.save()

        task_from_dbb = Task.objects.get(pk=child_task.id)
        self.assertEqual(task_from_dbb.parent, parent_task )




class TaskViewTests(TestCase):

    def test_should_get_index_view(self):
        response = self.client.get(reverse('tasks:index'))
        self.assertEqual(response.status_code, 200)



    def test_should_get_detail_view(self):
        task = Task(parent=None, name="name", description="description")
        task.save()
        response = self.client.get(reverse('tasks:detail', kwargs={ 'pk' : task.id}) )
        self.assertEqual(response.status_code, 200)
