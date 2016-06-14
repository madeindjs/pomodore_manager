#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sqlite3


class Database:

	# def loud_decorator(func):
	# 	def decorated(*args, **kwargs):
	# 		print("Now calling {0} with {1},{2}".format(func, args, kwargs))
	# 		return func(*args, **kwargs)
	# 	return decorated

	
	def __init__(self):
		try:
			self.connection = sqlite3.connect('data.sqlite')
			self.cursor = self.connection.cursor()
			self.cursor.execute(""" CREATE TABLE IF NOT EXISTS tasks( 
					id INTEGER PRIMARY KEY,
					node_id INTERGER NOT NULL default 0,
					name TEXT NOT NULL default 'no name',
					description TEXT default '',
					status INTEGER DEFAULT 0
					) """ )
			self.cursor.execute(""" CREATE TABLE IF NOT EXISTS pomodores( 
					id INTEGER PRIMARY KEY,
					task_id INTERGER NOT NULL,
					date TEXT NOT NULL
					) """ )
		except sqlite3.Error :
			raise e


	def __del__(self):
		self.cursor.close()

	# @loud_decorator
	# def read(self , query , data=None):
	# 	print('called')