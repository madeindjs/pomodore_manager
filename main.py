#!/usr/bin/env python
# -*- coding: utf-8 -*-
from classes.pomodore import Pomodore
from classes.task import Task
from classes.drawer import Drawer



def ask_user(list):
	Drawer().list( list )

	try:
		choice = int( input('What do you want to do? ') )
	except:
		print("Are you stupid?")

	if choice in list.keys():
		return choice
	else:
		print("Are you stupid?")
		return False

def start():

	Drawer().subheader("menu")

	choices = { 1: "Begin a Pomodore"  , 2: "add a task" , 3: "create a category" , 4: "add a task"}
	result = ask_user(choices) 

	if result == 1:
		Pomodore().add()

# Pomodore().add()

Drawer().header("POMODORE_MANAGER")
start()






