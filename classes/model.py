#!/usr/bin/env python
# -*- coding: utf-8 -*-
from classes.database import Database

class Model():
	"""
	Model class is the parent class for all object will contact database
	"""
	table_name = None # set by child
	attrs = list() # attributes will be set automatiquelly
	database = Database()


	def __init__(self, id=None, sql_row=None):
		"""initialize object from None or by sql_row if it pased in parameters"""
		if id:
			self.find_by('id', id)
		elif sql_row:
			self.set_from_sql_row(sql_row)
		else:
			for attr in self.attrs:
				setattr(self, attr, None)


	def find_by(self, column, value):
		"""find one item  by colum name & value"""
		data = {column : value}
		sql_query = "SELECT * FROM {0} WHERE {1} = :{1} LIMIT 1".format(self.table_name, column)
		data = self.database.cursor.execute( sql_query , data ).fetchone()

		if data:
			self.set_from_sql_row(data)
			return self
		else:
			return None


	def set_from_sql_row(self, sql_row):
		"""set all attributes from sql query data"""
		i = 0
		for column in sql_row:
			setattr(self, self.attrs[i], column)
			i += 1


	def delete(self):
		try:
			data = {'id': self.id}
			sql_query = "DELETE FROM {} WHERE id = :id".format(self.table_name)
			self.database.cursor.execute( sql_query , data )
			self.database.connection.commit()
			return True

		except AttributeError:
			print('Object have not id property')
			return False


	def add(self):
		"""add the current object in the database"""

		# get columns name & delete id (because it will be set automatiquelly by SQLite)
		inserted_columns = list(self.attrs)
		inserted_columns.pop(0)
		# build data into a dictionnary
		data = dict()
		for inserted_column in inserted_columns:
			data[inserted_column] = getattr(self, inserted_column)
		# build SQL query
		sql_query = 'INSERT INTO {table}({columns}) VALUES(:{columns_with_dots})'.format(
			table=self.table_name,
			columns=", ".join(inserted_columns),
			columns_with_dots=", :".join(inserted_columns)
		)
		# execute SQL query and find id inserted to update self Model
		if self.database.cursor.execute( sql_query , data ):
			sql_query = "SELECT id FROM {} ORDER BY id DESC LIMIT 1".format(self.table_name)
			id = self.database.cursor.execute(sql_query).fetchone()
			self.id = id[0]
			self.database.connection.commit()
		else:
			return False

	def update(self):
		"""update all columns from the current object values
		begin to build SQL query like `UPDATE tasks SET foo=:foo, bar=:bar WHERE id = :id`
		then execute it and return True or False"""
		
		# build data into a dictionnary like `{'foo': self.foo, 'bar': self.bar}`
		data = dict()
		for attr in list(self.attrs):
			data[attr] = getattr(self, attr)
		
		# build `..SET..` query like `SET foo=:foo, bar=:bar`
		updated_columns = list(self.attrs)
		updated_columns.pop(0)# remove `id` column
		sql_query = 'UPDATE {table} SET '.format(table=self.table_name)
		for updated_column in updated_columns:
			sql_query += '{column} = :{column}, '.format(column=updated_column)


		# finish to build sql_query
		sql_query = sql_query[:-2] # delete last `,`
		sql_query += ' WHERE id = :id'
		print(sql_query)
		print(data)

		# execute SQL query and find id inserted to update self Model
		try:
			self.database.cursor.execute( sql_query , data )
			self.database.connection.commit()
			return True
		except Exception as e:
			raise e
			return False



	@classmethod
	def all(cls):
		"""return all self object present in database"""
		sql_query = "SELECT id FROM {}".format(cls.table_name)
		for id in cls.database.cursor.execute("SELECT id FROM tasks").fetchall():
			yield cls(id=id[0]) 
