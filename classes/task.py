#!/usr/bin/env python
# -*- coding: utf-8 -*-

from classes.database import *
from classes.category import *



class Task(Database):

	DATABASE_NAME = 'tasks'


	def add(self ,  name , category):
		# check before if this category already exist
		data = { "name" : name , "category_id" : category.id }
		self.cursor.execute("INSERT INTO tasks(category_id, name) VALUES(:category_id, :name)" , data )
		self.connection.commit()
		#set up & check if saved succesfully
		if self.find_by_name(name):
			return self
		else:
			return False




	def set(self, data):
		self.id = data[0]
		self.category = Category().find_by_id(data[1])
		self.name = data[2]
		return self

	def describe(self):
		if self.category is None:
			return False
		else:
			return "#{} in {}: {} = {} pomodores".format( self.id, self.category.name, self.name,  self.count_pomodores() )


	def count_pomodores(self):

		if not self.id is None:
			data = { 'task_id' : self.id }
			self.cursor.execute("SELECT COUNT(*) from pomodores WHERE task_id = :task_id " , data )
			result = self.cursor.fetchone()
			return result[0]
		else:
			return False

	def list(self):
		# Drawer().subheader(self.DATABASE_NAME)
		self.cursor.execute( "SELECT * FROM {}".format( self.DATABASE_NAME ) )
		tasks = [] 

		for row in self.cursor:
			task_temp = Task().set(row)
			tasks.append(task_temp.describe())
			# print("Task N°{} # {}   | {}".format( task_temp.id , task_temp.category.name , 'o'*task_temp.count_pomodores() ))
			# print("    {}\n".format(task_temp.name))

		return tasks
