#!/usr/bin/env python
# -*- coding: utf-8 -*-

from classes.record import Record
from classes.database import Database


class Category(Record):

	def __init__(self):
		self.database = Database('categories')


	def read(self, id):
		data = self.database.find_by_('id', id)
		self.id = data[0][0]
		self.name = data[0][1]

	def create(self):
		pass








	# def create(self, name):
	# 	# check before if this category already exist
	# 	if self.read(name) == False:
	# 		data = { "name" : name }
	# 		self.cursor.execute("INSERT INTO categories(name) VALUES( :name)" , data )
	# 		self.connection.commit()
	# 		#set up & check if saved succesfully
	# 		if self.find_by_name(name):
	# 			return self
	# 		else:
	# 			return False

	# 	else:
	# 		return False

	# def read(self, database, id=None, name=None):

	# 	if id is not None:
	# 		sql_command = "SELECT * FROM {} WHERE {} = :{} LIMIT 1".format( self.DATABASE_NAME , column , column )
	# 		self.cursor.execute( sql_command , data )

	# 	elif name is not None:

	# 	else:
	# 		print("You need a ")
	# 		return False

	# def update():
	# 	pass

	# def delete():
	# 	pass



	# def create(self,  name):




	# def set(self, data):
	# 	self.id = data[0]
	# 	self.name = data[1]
	# 	return self

	# def describe(self):
	# 	return "Category #{} named *{}*".format(self.id, self.name) 
