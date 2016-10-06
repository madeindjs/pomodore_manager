from django.db import models


class Task(models.Model):
    """a task is something to do. Task can also have a parent task in this way
    it become a sub-task"""
    parent = models.ForeignKey("self", null=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=250)



    def __str__(self):
        return self.name