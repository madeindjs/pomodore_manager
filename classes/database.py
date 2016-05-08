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

	def __init__(self , name ):
		try:
			self._open()
		except:
			print('error in database connection')

		self.name = name

	def find_by_(self, column, column_data ):
		data = { column : column_data }
		sql_command = "SELECT * FROM {0} WHERE {1} = :{1} LIMIT 1".format( self.name, column )
		self.cursor.execute( sql_command , data )
		return self.cursor.fetchall()



	def add_task():
		pass

	def add_pomodore():
		pass

	def add_category():
		pass


	def __del__(self):
		self.cursor.close()

	def _open(self):
		self.connection = sqlite3.connect('databases.sqlite')
		self.cursor = self.connection.cursor()

	def _create_databases(self):
		self.cursor.execute(
			"CREATE TABLE IF NOT EXISTS categories( " + 
				"id INTEGER PRIMARY KEY , "+
				"name TEXT NOT NULL UNIQUE) ")