from django.conf.urls import url
from . import views

app_name = 'tasks'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    # ex: /tasks/5/
    url(r'^(?P<task_id>[0-9]+)/$', views.detail, name='detail'),

]