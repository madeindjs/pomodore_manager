#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime

from view.writter import Writter

from classes.model import Model
from classes.worktime import WorkTime

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


	@property
	def worktimes(self):
		"""generator wortimes"""
		data = { "task_id" : self.id}
		sql_query = "SELECT id, task_id FROM worktimes WHERE task_id=:task_id"
		result = self.database.cursor_execute( sql_query , data ).fetchall()
		for id in result:
			yield WorkTime(id=id[0])



	@property
	def spended_time(self):
		"""return the total time spend on this task"""
		time_delta = 0
		for worktime in self.worktimes:
			time_delta += worktime.end - worktime.begin

		return datetime.timedelta(seconds=time_delta)
	
