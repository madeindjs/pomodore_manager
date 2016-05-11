#!/usr/bin/env python
# -*- coding: utf-8 -*-
from classes.database import Database

class Task():


	def __init__(self , id=None, name="no_name", node_id=0):
		self.database = Database()

		if id is not None:#if id is set, we retreive it from database
			self.find('id' , id)
		
		else:#else, we add it into database
			self.name = name
			self.node_id = node_id
			self.add()

	def __del__(self):
		del(self)


	def all():
		tasks=[]
		database = Database()

		for id in database.cursor.execute("SELECT id FROM tasks").fetchall():
			tasks.append( Task(id[0]) )

		return tasks


	def add(self):
		# add the item
		data = { "name" : self.name , "node_id" : self.node_id }
		self.database.cursor.execute("INSERT INTO tasks(node_id, name) VALUES(:node_id, :name)" , data )
		self.database.connection.commit()

		# I retreive the id saved
		self.database.cursor.execute("SELECT id FROM tasks ORDER BY id DESC LIMIT 1" )
		self.id = self.database.cursor.fetchone()[0]

		#set up & check if saved succesfully
		if self.find('id' , self.id):
			return self
		else:
			return False

	def rename(self, new_name):
		self.name = new_name
		# add the item
		data = { "name" : self.name , "id" : self.id}
		
		self.database.cursor.execute("UPDATE tasks SET name=:name WHERE id = :id" , data )
		self.database.connection.commit()

	def delete(self):
		data = { "id" : self.id}
		sql_query = "DELETE FROM tasks WHERE id = :id OR node_id = :id"
		self.database.cursor.execute( sql_query , data )
		self.database.connection.commit()

		self.__del__()



	def find(self, column, column_data ):
		data = { column : column_data }
		sql_command = "SELECT * FROM tasks WHERE {0} = :{0} LIMIT 1".format(column)
		self.database.cursor.execute( sql_command , data )

		result = self.database.cursor.fetchone()
		if result is None:
			return False
		else:
			self.id = result[0]
			self.node_id = result[1]
			self.name = result[2]
			return self


	def describe(self):
		try:
			return "Task #{} named {}".format(self.id, self.name)
		except AttributeError:
			print('object not set')
