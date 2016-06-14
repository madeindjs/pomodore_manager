import os
import unittest
import shutil

import json
import re

import classes
from classes.database import Database
from classes.task import Task



class ModelTest(unittest.TestCase):

	model = None

	def setUp(self):
		Task.database = Database('data/test.sqlite')
		self.model = Task()
		self.model.name = "task_test"
		self.model.node_id = 0



	def test_check_tables_exists(self):
		"""check if table exists in database with a simple SQL query"""
		sql_query = """SELECT name  FROM sqlite_master 
						WHERE type='table' AND name='{table}'
						""".format(table=Task.table_name)
		self.assertIsNotNone( self.model.database.cursor.execute( sql_query ).fetchone() )



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



	def test_task_delete_also_subtasks_to_database(self):
		"""check if number of rows before and after delete change"""
		# add task & subtasks
		self.model.add()
		subtasks = Task()
		subtasks.name = "subtask_test"
		subtasks.node_id = self.model.id
		subtasks.add()
		subtasks.add()
		# delete and search tasks
		data = {'node_id': self.model.id}
		self.model.delete()
		sql_query = "SELECT COUNT(*) FROM {} WHERE node_id = :node_id".format(self.model.table_name)
		count = self.model.database.cursor.execute( sql_query, data ).fetchone()
		self.assertEqual(count[0], 0)



	def test_all_method(self):
		"""check if all method return same qty objects than COUNT(*)"""
		sql_query = "SELECT COUNT(*) FROM {}".format(self.model.table_name)
		count = self.model.database.cursor.execute( sql_query ).fetchone()
		model_class = self.model.__class__
		self.assertEqual( count[0] , len(list(model_class.all())))





if __name__ == '__main__':
	unittest.main()
