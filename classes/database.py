import sqlite3

class Database:

	def __init__(self):
		try:
			self.connection = sqlite3.connect('databases.sqlite')
			self.cursor = self.connection.cursor()
			self.cursor.execute("CREATE TABLE IF NOT EXISTS users( id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,name TEXT,age INTERGER ) ")
		except:
			print('error in database creation')

		print('database initialized')

	def insert(self , data):
		self.cursor.execute("INSERT INTO users(name, age) VALUES(:name, :age)", data)
		self.connection.commit()

	def read_data(self):
		self.cursor.execute("""SELECT * FROM users""")

		for row in self.cursor:
			print( 'id:{0} | nom:{1} | age:{2}'.format(row[0], row[1], row[2]))


