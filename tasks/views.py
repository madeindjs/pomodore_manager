from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from django.views import generic
from django.urls import reverse
from .models import Task



class IndexView(generic.ListView):
    template_name = 'tasks/index.html'
    context_object_name = 'latest_tasks'

    def get_queryset(self):
        return Task.objects.order_by('id')[:5]



class DetailView(generic.DetailView):
    model = Task
    template_name = 'tasks/detail.html'



def new (request):
    if request.method == 'GET':
        template = loader.get_template('tasks/new.html')
        context = {'tasks': Task.objects.all(), }
        return HttpResponse(template.render(context, request))

    elif request.method == 'POST':
        try:
            parent_task = Task.objects.get(pk=request.POST.get("parent_id", 0))
        except Task.DoesNotExist as e:
            parent_task = None
        

        new_task = Task(name=request.POST.get("title", "no title"),
            description=request.POST.get("description", "no description"),
            parent=parent_task)

        new_task.save()
        return HttpResponseRedirect(reverse('tasks:detail', args=(new_task.id,)))

