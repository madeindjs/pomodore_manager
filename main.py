#!/usr/bin/env python
# -*- coding: utf-8 -*-
from classes.category import Category
from classes.task import Task


category = Category()
category.add('PYT')
# category.add(input('Write a name for your category: '))

task = Task()
task.add("Build a plugin" , category )
print(task.describe())

# category.find_by_name('YT')
# category.find_by_name('WEB')


# category.list()