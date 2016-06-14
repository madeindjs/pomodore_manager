#!/usr/bin/env python
# -*- coding: utf-8 -*-
from classes.objects.model import Model
from classes.objects.pomodore import Pomodore

class Task(Model):

	table_name = 'tasks'
	attrs = ['id', 'node_id', 'name', 'description', 'status']


	def delete(self):
		for task in self.subtasks():
			task.delete()

		Model(self).delete()



	def subtasks(self):
		data = { "id" : self.id}
		tasks = []
		sql_query = "SELECT id FROM tasks WHERE node_id = :id"
		result = self.database.cursor.execute( sql_query , data ).fetchall()
		for id in result:
			tasks.append(Task(id[0]))
		return tasks


	def count_pomodores(self):
		data = { 'task_id' : self.id }
		sql_command = "SELECT COUNT(*) FROM pomodores WHERE task_id = :task_id"
		result = self.database.cursor.execute( sql_command , data ).fetchone()
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
