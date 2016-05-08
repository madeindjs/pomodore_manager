#!/usr/bin/env python
# -*- coding: utf-8 -*-

from classes.database import *
from classes.task import *


class Category(Database):

	DATABASE_NAME = 'categories'

	def __init__(self):
		Database.__init__(self)
		self.cursor.execute(
			"CREATE TABLE IF NOT EXISTS categories( " + 
				"id INTEGER PRIMARY KEY , "+
				"name TEXT NOT NULL UNIQUE) ")


	def add(self ,  name ):
		# check before if this category already exist
		if self.find_by_name(name) == False:
			data = { "name" : name }
			self.cursor.execute("INSERT INTO categories(name) VALUES( :name)" , data )
			self.connection.commit()
			#set up & check if saved succesfully
			if self.find_by_name(name):
				return self
			else:
				return False

		else:
			return False


	def set(self, data):
		self.id = data[0]
		self.name = data[1]
		return self

	def describe(self):
		return "Category #{} named *{}*".format(self.id, self.name) 

	def tasks_id(self):
		if self.id is not None:
			data = { 'category_id' : self.id }
			sql_command = "SELECT id FROM tasks WHERE category_id = :category_id"

			self.cursor.execute( sql_command , data )

			return self.cursor.fetchall()
		else:
			print('this category is not set')

