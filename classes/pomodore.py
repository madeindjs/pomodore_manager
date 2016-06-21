#!/usr/bin/env python
# -*- coding: utf-8 -*-

#import tkinter interface

from classes.database import Database
import datetime


class Pomodore():
	"""a Pomodore is a time for a task. During this timer, you'll work only on
	this task"""
	database = Database()



	def __init__(self, task):
		self.task = task



	def add(self):
		data = { "task_id" : self.task.id , "date" : datetime.datetime.today() }
			
		database = Database()
		database.cursor.execute("INSERT INTO pomodores(task_id, date) VALUES(:task_id, :date)" , data )
		database.connection.commit()