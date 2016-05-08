#!/usr/bin/env python
# -*- coding: utf-8 -*-
from classes.pomodore import Pomodore
from classes.task import Task
from classes.category import Category
from classes.drawer import Drawer
from classes.interface import Interface

category = Category().add("WEB")
category = Category().add("PYT")
category = Category().add("TEST")
category = Category().add("HELL")


Task().add("Use Tkinter" , category )
Task().add("Play with Tkinter" , category )


categories = Category().all()
print('-------')
for category in categories:
	print(category.describe())

interface = Interface()



# interface.add_label(tasks)
# interface.add_label("comment ca va?")
interface.show()

