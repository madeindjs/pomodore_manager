import sqlite3

class Database:

	def __init__(self):
		try:
			self.connection = sqlite3.connect('databases.sqlite')
			self.cursor = self.connection.cursor()
		except:
			print('error in database connection')


	def __del__(self):
		self.cursor.close()

	def _open(self):
		self.connection = sqlite3.connect('databases.sqlite')
		self.cursor = self.connection.cursor()


	# to check if cursor have at less one row
	def is_data_exists(cursor):
		result = cursor.fetchone()
		if result is None:
			return False
		else:
			return True
