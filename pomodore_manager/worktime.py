#!/usr/bin/env python
# -*- coding: utf-8 -*-

#import tkinter interface

from .database import Database
from .model import Model

import time
import datetime


class WorkTime(Model):
	"""a work time is a time spend on one task"""
	database = Database()
	table_name = 'worktimes'
	attrs = ['id', 'task_id', 'begin', 'end']



	def __init__(self, task=None, id=None, sql_row=None):
		if id:
			self.find_by('id', id)

		elif sql_row:
			self.set_from_sql_row(sql_row)

		elif task:
			self.task_id = task.id
			self.begin = time.time()
		



	def add(self):
		"""add current date time to end property and add it to the database"""
		self.end = time.time()
		super(WorkTime, self).add()



	def update(self):
		raise NotImplementedError



	@classmethod
	def all(cls):
		raise NotImplementedError



	def spend_from_now(self):
		"""return a string in HH:MM:SS spend from now"""
		time_delta = time.time() - self.begin
		return datetime.timedelta(seconds=time_delta)


	@property
	def time(self):
		"""return time spend on this work time in seconds"""
		return self.end - self.begin


