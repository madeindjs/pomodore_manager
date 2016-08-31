import os
import unittest
import shutil

import json
import re

import classes
from classes.database import Database
from classes.task import Task
from classes.worktime import WorkTime



class WorkTimeTest(unittest.TestCase):

	model = None

	def setUp(self):
		WorkTime.database = Database('data/test.sqlite')
		task = Task()
		task.id = 1
		self.model = WorkTime(task)



	def test_check_tables_exists(self):
		"""check if table exists in database with a simple SQL query"""
		sql_query = """SELECT name  FROM sqlite_master 
						WHERE type='table' AND name='{table}'
						""".format(table=WorkTime.table_name)
		self.assertIsNotNone( self.model.database.cursor_execute( sql_query ).fetchone() )



	def test_model_can_be_added_in_database(self):
		"""check number of rows before and after insertion"""
		sql_query = "SELECT COUNT(id) FROM {}".format(self.model.table_name)
		old_count = self.model.database.cursor.execute( sql_query ).fetchone()
		self.model.add()
		new_count = self.model.database.cursor.execute( sql_query ).fetchone()
		self.assertEqual(old_count[0]+1, new_count[0])



	def test_model_can_be_finded(self):
		"""add an object find a random id in database and check if find() method can find it"""
		sql_query = "SELECT id FROM {} LIMIT 1".format( self.model.table_name)
		id = self.model.database.cursor.execute( sql_query ).fetchone()
		sql_result =  self.model.find_by( 'id', id[0] )
		self.assertIsNotNone( sql_result )


	
	def test_model_can_be_deleted_to_database(self):
		"""check if number of rows before and after delete change"""
		sql_query = "SELECT COUNT(id) FROM {}".format(self.model.table_name)
		old_count = self.model.database.cursor.execute( sql_query ).fetchone()
		self.model.add()
		self.model.delete()
		new_count = self.model.database.cursor.execute( sql_query ).fetchone()
		self.assertEqual(old_count[0], new_count[0])

