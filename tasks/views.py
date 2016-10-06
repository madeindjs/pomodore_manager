from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader
from .models import Task


def index(request):
    latest_tasks = Task.objects.order_by('id')[:5]
    template = loader.get_template('tasks/index.html')
    context = {'latest_tasks': latest_tasks, }
    return HttpResponse(template.render(context, request))

def detail(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    template = loader.get_template('tasks/details.html')
    context = {'task': task, }
    return HttpResponse(template.render(context, request))