#!/usr/bin/env python
# -*- coding: utf-8 -*-
from view.writter import Writter

from classes.model import Model

class Task(Model):

	table_name = 'tasks'
	attrs = ['id', 'node_id', 'name', 'description', 'status']


	def delete(self):
		"""delete task and also subtasks"""
		Writter.event('delete task n°{} and subtasks linked'.format(self.id))

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
		"""return all subtasks linked to this task"""
		Writter.event('delete task n°{} and subtasks linked'.format(self.id))

		data = { "id" : self.id}
		sql_query = "SELECT id FROM tasks WHERE node_id = :id"
		result = self.database.cursor_execute( sql_query , data ).fetchall()
		for id in result:
			yield tasks.append(Task(id[0]))


	def count_pomodores(self):
		"""return count of pomodores linked"""
		data = { 'task_id' : self.id }
		sql_command = "SELECT COUNT(*) FROM pomodores WHERE task_id = :task_id"
		result = self.database.cursor_execute( sql_command , data ).fetchone()
		return result[0]




	def start(self):
		if Pomodore(self):
			print('task finished')
