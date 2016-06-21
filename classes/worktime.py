#!/usr/bin/env python
# -*- coding: utf-8 -*-

#import tkinter interface

from classes.database import Database
from classes.model import Model

import time
import datetime


class WorkTime(Model):
	"""a work time is a time spend on one task"""
	database = Database()
	table_name = 'worktimes'
	attrs = ['id', 'task_id', 'begin', 'end']



	def __init__(self, task):
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
		return  datetime.timedelta(seconds=time_delta)

