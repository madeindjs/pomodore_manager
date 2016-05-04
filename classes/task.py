from classes.database import Database

class Task(Database):

	def __init__(self):
		Database.__init__(self)
		self.cursor.execute(
			"CREATE TABLE IF NOT EXISTS tasks( " + 
				"id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, "+
				"category_id INTERGER NOT NULL, "+
				"name TEXT NOT NULL , description TEXT ) ")


	def find(self):
		print("hello world")


	# def add(self ,  name ):
	# 	data = { "name" : name }
	# 	self.cursor.execute("INSERT INTO categories( name) VALUES( :name)" , data )
	# 	self.connection.commit()

	def list(self):
		self.cursor.execute( "SELECT * FROM tasks" )
		for row in self.cursor:
			print( row )