from classes.database import Database

class Category(Database):

	def __init__(self):
		Database.__init__(self)
		self.cursor.execute(
			"CREATE TABLE IF NOT EXISTS categories( " + 
				"id INTEGER PRIMARY KEY , "+
				"name TEXT NOT NULL ) ")


	def find(self):
		print("hello world")


	def add(self ,  name ):
		data = { "name" : name }
		self.cursor.execute("INSERT INTO categories( name) VALUES( :name)" , data )
		self.connection.commit()

	def list(self):
		self.cursor.execute( "SELECT * FROM categories" )
		for row in self.cursor:
			print( row )