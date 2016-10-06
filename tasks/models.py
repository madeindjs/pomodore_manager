from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)



    def __str__(self):
        return self.name




class Task(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=250)



    def __str__(self):
        return self.name