#!/usr/bin/env python
# -*- coding: utf-8 -*-

#import tkinter interface

from classes.objects.database import Database
import datetime


class Pomodore():

	database = Database()

	def __init__(self, task):
		self.task = task

	def add(self):
		data = { "task_id" : self.task.id , "date" : datetime.datetime.today() }
			
		database = Database()
		database.cursor.execute("INSERT INTO pomodores(task_id, date) VALUES(:task_id, :date)" , data )
		database.connection.commit()