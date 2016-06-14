#!/usr/bin/env python
# -*- coding: utf-8 -*-
from classes.model import Model
from classes.pomodore import Pomodore

class Task(Model):

	table_name = 'tasks'
	attrs = ['id', 'node_id', 'name', 'description', 'status']


	def delete(self):
		"""delete task and also subtasks"""
		try:
			data = {'id': self.id , 'node_id': self.id}
			sql_query = "DELETE FROM {} WHERE id = :id OR node_id = :node_id".format(self.table_name)
			self.database.cursor_execute( sql_query , data )
			self.database.connection.commit()
			return True

		except AttributeError:
			print('Object have not id property')
			return False



	def subtasks(self):
		data = { "id" : self.id}
		sql_query = "SELECT id FROM tasks WHERE node_id = :id"
		result = self.database.cursor_execute( sql_query , data ).fetchall()
		for id in result:
			yield tasks.append(Task(id[0]))


	def count_pomodores(self):
		data = { 'task_id' : self.id }
		sql_command = "SELECT COUNT(*) FROM pomodores WHERE task_id = :task_id"
		result = self.database.cursor_execute( sql_command , data ).fetchone()
		return result[0]



	def describe(self):
		try:
			return self.name
			# return "{} # {}".format(self.id, self.name)
		except AttributeError:
			print('object not set')


	def start(self):
		if Pomodore(self):
			print('task finished')
