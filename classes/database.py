import sqlite3

class Database:

	def __init__(self):
		try:
			self.connection = sqlite3.connect('databases.sqlite')
			self.cursor = self.connection.cursor()

			self.cursor.execute(
				"CREATE TABLE IF NOT EXISTS tasks( " + 
					"id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, "+
					"category_id INTERGER NOT NULL, "+
					"name TEXT NOT NULL , description TEXT ) ")



			self.cursor.execute(
				"CREATE TABLE IF NOT EXISTS pomodores( " + 
					"id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, "+
					"task_id INTERGER NOT NULL, "+
					"category_id INTERGER NOT NULL, "+
					"date DATETIME ) ")

		except:
			print('error in database creation')


	def __del__(self):
		self.cursor.close()

	def _open(self):
		self.connection = sqlite3.connect('databases.sqlite')
		self.cursor = self.connection.cursor()


		
