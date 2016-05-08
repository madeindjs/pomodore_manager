#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3


class Database:
	"""
	This is a Parent class for:
		* Categoy
		* Task
		* Pomodore
	She is used to reduce similar code between theses classes and make cleaner code
	"""

	DATABASE_NAME = None

	def __init__(self , id = None):
		try:
			self.connection = sqlite3.connect('databases.sqlite')
			self.cursor = self.connection.cursor()
		except:
			print('error in database connection')

		if id is not None:
			self.find_by_id(id)


	def __del__(self):
		self.cursor.close()

	def _open(self):
		self.connection = sqlite3.connect('databases.sqlite')
		self.cursor = self.connection.cursor()



	def find_by_(self, column, column_data ):
		data = { column : column_data }
		sql_command = "SELECT * FROM {} WHERE {} = :{} LIMIT 1".format( self.DATABASE_NAME , column , column )
		self.cursor.execute( sql_command , data )
		return self.is_data_exists( self.cursor )


	def find_by_id(self,  id_to_find ):
		return Database.find_by_(self, 'id', id_to_find )


	def find_by_name(self,  name_to_find ):
		return Database.find_by_( self, 'name', name_to_find )


	# to check if cursor have at less one row
	def is_data_exists(self , cursor):
		result = cursor.fetchone()
		if result is None:
			return False
		else:
			# if data exists, we set the object with values
			return self.set(result)



	def all(self):
		all_item = []
		self.cursor.execute( "SELECT id FROM {}".format( self.DATABASE_NAME ) )
		
		data = self.cursor.fetchall()

		for row in data :
			print( self.find_by_id(row[0]).describe() )
			# problem here
			all_item.append( self.find_by_id(row[0]) )

		return all_item


