#!/usr/bin/env python
# -*- coding: utf-8 -*-

from classes.database import Database
from classes.task import Task

class Node():

	def __init__(self , id=0):
		self.database = Database()
		self.id = id

	def all(self):
		nodes=[]
		for data in self.database.cursor.execute("SELECT node_id FROM tasks GROUP BY node_id").fetchall():
			nodes.append(Node(data[0]))

		return nodes

	# to return each tasks at this node
	def tasks(self):
		tasks=[]
		data = {'node_id' : self.id }
		self.database.cursor.execute("SELECT * FROM tasks WHERE node_id = :node_id" , data )
		
		for id in self.database.cursor.fetchall():
			tasks.append( Task(id[0]) )

		return tasks
