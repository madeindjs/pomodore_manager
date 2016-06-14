#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sqlite3


class Database:

	verbose = False

	def __init__(self , file='data/data.sqlite'):
		self.file = file
		try:
			self.connection = sqlite3.connect(self.file)
			self.cursor = self.connection.cursor()
			self._init_tables()
		except sqlite3.Error :
			raise e



	def __del__(self):
		self.cursor.close()



	def _init_tables(self):
		try:
			self.cursor_execute(""" CREATE TABLE IF NOT EXISTS tasks( 
					id INTEGER PRIMARY KEY,
					node_id INTERGER NOT NULL default 0,
					name TEXT NOT NULL default 'no name',
					description TEXT default '',
					status INTEGER DEFAULT 0
					) """ )
			self.cursor_execute(""" CREATE TABLE IF NOT EXISTS pomodores( 
					id INTEGER PRIMARY KEY,
					task_id INTERGER NOT NULL,
					date TEXT NOT NULL
					) """ )
		except sqlite3.Error :
			raise e


	def cursor_execute(self, sql_query , data=None):
		"""an overwride function for `cursos.execute` to print each query"""
		if self.verbose:
			print(sql_query)

		# run SQL query normally
		if data:
			return self.cursor.execute(sql_query, data)
		else:
			return self.cursor.execute(sql_query)





