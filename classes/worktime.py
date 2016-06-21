#!/usr/bin/env python
# -*- coding: utf-8 -*-

#import tkinter interface

from classes.database import Database
from classes.model import Model
import time


class WorkTime(Model):
	"""a work time is a time spend on one task"""
	database = Database()
	table_name = 'worktimes'
	attrs = ['id', 'task_id', 'begin', 'end']



	def __init__(self, task):
		self.task_id = task.id
		self.begin = self._current_timestamp



	def add(self):
		"""add current date time to end property and add it to the database"""
		self.end = self._current_timestamp
		super(WorkTime, self).add()



	@property
	def _current_timestamp(self):
		current_time = time.localtime()
		return time.mktime(current_time)



	def update(self):
		raise NotImplementedError



	@classmethod
	def all(cls):
		raise NotImplementedError

