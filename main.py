#!/usr/bin/env python
# -*- coding: utf-8 -*-
from classes.pomodore import Pomodore
from classes.task import Task
from classes.category import Category
from classes.drawer import Drawer
from classes.interface import Interface

category = Category().add("WEB")
Task().add("Use Tkinter" , category )
Task().add("Play with Tkinter" , category )

interface = Interface()
interface.add_list(Task().list())


# interface.add_label(tasks)
# interface.add_label("comment ca va?")
interface.show()



# def ask_user(list):
# 	Drawer().list( list )

# 	try:
# 		choice = int( input('What do you want to do? ') )
# 	except:
# 		print("Are you stupid?")

# 	if choice in list.keys():
# 		return choice
# 	else:
# 		print("Are you stupid?")
# 		return False

# def start():

# 	Drawer().subheader("menu")

# 	choices = { 
# 			1: "Begin a Pomodore"  , 
# 			2: "add a task" , 
# 			3: "create a category" , 
# 			4: "add a task" , 
# 			5: "list pomodore" , 
# 			6: "list tasks",
# 			666: "exit"
# 		}
# 	result = ask_user(choices) 

# 	if result == 1:
# 		Pomodore().add()

# 	elif result == 2 :
# 		category = Category().select()
# 		if category:
# 			Task().add( input('Enter a name for your task: ') , category )


# 	elif result == 5 :
# 		Pomodore().list()

# 	elif result == 6:
# 		Task().list()

# 	elif result == 666:
# 		return #to exit

# 	start()


# # Pomodore().add()

# Drawer().header("POMODORE_MANAGER")
# start()






