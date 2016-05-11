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

	def __init__(self):
		try:
			self.connection = sqlite3.connect('databases.sqlite')
			self.cursor = self.connection.cursor()
			self.cursor.execute(
				""" CREATE TABLE IF NOT EXISTS tasks( 
					id INTEGER PRIMARY KEY,
					node_id INTERGER NOT NULL default 0,
					name TEXT NOT NULL, 
					description TEXT default ''
					) """ )
		except:
			print('error in database connection')


	def __del__(self):
		self.cursor.close()