#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3
from classes.drawer import Drawer


class Database:
	"""
	This is a Parent class for:
		* Categoy
		* Task
		* Pomodore
	She is used to reduce similar code between theses classes and make cleaner code
	"""

	DATABASE_NAME = None

	def __init__(self):
		try:
			self.connection = sqlite3.connect('databases.sqlite')
			self.cursor = self.connection.cursor()
		except:
			print('error in database connection')


	def __del__(self):
		self.cursor.close()

	def _open(self):
		self.connection = sqlite3.connect('databases.sqlite')
		self.cursor = self.connection.cursor()



	def find_by_(self, database, column, column_data ):
		data = { column : column_data }
		sql_command = "SELECT * FROM {} WHERE {} = :{} LIMIT 1".format( database , column , column )
		self.cursor.execute( sql_command , data )
		return self.is_data_exists( self.cursor )


	def find_by_id(self,  id_to_find ):
		return Database.find_by_(self, self.DATABASE_NAME, 'id', id_to_find )


	def find_by_name(self,  name_to_find ):
		return Database.find_by_( self, self.DATABASE_NAME,  'name', name_to_find )


	# to check if cursor have at less one row
	def is_data_exists(self , cursor):
		result = cursor.fetchone()
		if result is None:
			return False
		else:
			# if data exists, we set the object with values
			self.set(result)
			return self

	# we can't set database object with this method
	# this method is reserved for child (cetgory, tasks, etc..)
	def set():
		print("Can't set up database. Ensure you use a child of database")

	def list(self):
		Drawer().subheader(self.DATABASE_NAME)
		self.cursor.execute( "SELECT * FROM {}".format( self.DATABASE_NAME ) )
		for row in self.cursor:
			print( row )
		Drawer().line()


	# a function to ask user to select user in database
	def select(self):
		self.list()
		try:
			choice = int( input('Wich item choose? ') )
		except:
			print("Are you stupid?")

		if self.find_by_id(choice):
			return self
		else:
			return False


