#!/usr/bin/env python
# -*- coding: utf-8 -*-
from classes.pomodore import Pomodore
from classes.task import Task
from classes.category import Category
from classes.drawer import Drawer
from classes.interface import Interface

category = Category().add("WEB")
Task().add("Continue Raspberry Cook" , category )

category = Category().add("PYT")
Task().add("Play with Tkinter" , category )
Task().add("Use Tkinter" , category )

category = Category().add("GIT")
Task().add("Update on Github" , category )




interface = Interface()



# interface.add_label(tasks)
# interface.add_label("comment ca va?")
interface.show()

