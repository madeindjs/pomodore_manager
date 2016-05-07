#!/usr/bin/env python
# -*- coding: utf-8 -*-

from classes.database import Database
from classes.task import Task
from classes.timer import Timer
from classes.drawer import Drawer
import datetime

class Pomodore(Database):

	DATABASE_NAME = 'pomodores'
	POMODORE_TIME = 5

	def __init__(self):
		Database.__init__(self)
		self.cursor.execute(
			"CREATE TABLE IF NOT EXISTS pomodores( " + 
				"id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, "+
				"task_id INTERGER NOT NULL, "+
				"date DATETIME ) ")


	def add(self):
		#ask wich task
		task = Task()
		task.list()
		try:
			answer = int( input('Wich task do you work with (Enter nly the number)? ') )
			task.find_by_id(answer)
			print("You chose {}".format( task.describe()) )
		except:
			print("Please enter a valid value")

		#start the prompt
		loader = Timer(self.POMODORE_TIME)
		
		if loader.start():
			data = { "task_id" : task.id , "date" : datetime.datetime.now() }
			self.cursor.execute("INSERT INTO pomodores(task_id, date) VALUES(:task_id, :date)" , data )
			self.connection.commit()
			return True

		else:
			return False


	def set(self , data):
		self.id = data[0]
		self.task = Task().find_by_id(data[1])
		self.date = data[2]
		return self

	def describe(self):
		return("Pomodore about {} did {}".format(self.task.name , self.date  )) 



	def list(self):
		Drawer().subheader(self.DATABASE_NAME)
		self.cursor.execute( "SELECT * FROM {}".format( self.DATABASE_NAME ) )
		for row in self.cursor:
			pomodore_temp = Pomodore().find_by_id(  row[0] )
			print( pomodore_temp.describe() )
		Drawer().line()