#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sqlite3
from view.writter import Writter


class Database:
	"""database class to create an object for the sqlite file"""



	def __init__(self , file='data/data.sqlite'):
		self.file = file
		try:
			self.connection = sqlite3.connect(self.file)
			self.cursor = self.connection.cursor()
			self._init_tables()
		except sqlite3.Error as e:
			raise e



	def __del__(self):
		self.cursor.close()



	def _init_tables(self):
		"""check if tables exists and create them if not"""
		try:
			self.cursor_execute(""" CREATE TABLE IF NOT EXISTS tasks( 
					`id` INTEGER PRIMARY KEY,
					`node_id` INTEGER NOT NULL default 0,
					`name` TEXT NOT NULL default 'no name',
					`description` TEXT default '',
					`status` INTEGER DEFAULT 0
					) """ )
			self.cursor_execute(""" CREATE TABLE IF NOT EXISTS worktimes( 
					`id` INTEGER PRIMARY KEY,
					`task_id` INTEGER NOT NULL,
					`begin` REAL NOT NULL,
					`end` REAL NOT NULL
					) """ )
		except sqlite3.Error as e :
			raise e



	def cursor_execute(self, sql_query , data=None):
		"""an overwride function for `cursos.execute` to print each query"""

		Writter.sql_log(sql_query , data) 

		# run SQL query normally
		if data:
			return self.cursor.execute(sql_query, data)
		else:
			return self.cursor.execute(sql_query)
