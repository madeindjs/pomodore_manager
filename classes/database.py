import sqlite3

class Database:

	DATABASE_NAME = None

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



	def find_by_(self, database, column, column_data ):
		data = { column : column_data }
		sql_command = "SELECT * FROM {} WHERE {} = :{} LIMIT 1".format( database , column , column )
		self.cursor.execute( sql_command , data )
		return self.is_data_exists( self.cursor )


	def find_by_id(self,  id_to_find ):
		return Database.find_by_(self, self.DATABASE_NAME, 'id', id_to_find )


	def find_by_name(self,  name_to_find ):
		return Database.find_by_( self, self.DATABASE_NAME,  'name', name_to_find )


	# to check if cursor have at less one row
	def is_data_exists(self , cursor):
		result = cursor.fetchone()
		if result is None:
			return False
		else:
			return True

	def list(self):
		print('----------')
		print(self.DATABASE_NAME)
		print('----------')
		self.cursor.execute( "SELECT * FROM {}".format( self.DATABASE_NAME ) )
		for row in self.cursor:
			print( row )
		print('----------')

