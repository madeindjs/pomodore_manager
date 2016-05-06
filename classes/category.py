from classes.database import Database

class Category(Database):

	def __init__(self):
		Database.__init__(self)
		self.cursor.execute(
			"CREATE TABLE IF NOT EXISTS categories( " + 
				"id INTEGER PRIMARY KEY , "+
				"name TEXT NOT NULL UNIQUE) ")


	def find_by_id(self,  id ):
		data = { "id" : id }
		self.cursor.execute( "SELECT * FROM categories WHERE id = :id LIMIT 1" , data )
		return Database.is_data_exists( self.cursor )



	def find_by_name(self,  name ):
		data = { "name" : name }
		self.cursor.execute( "SELECT * FROM categories WHERE name = :name LIMIT 1" , data )
		return Database.is_data_exists( self.cursor )


	def add(self ,  name ):
		# check before if this category already exist
		if self.find_by_name(name) == False:
			data = { "name" : name }
			self.cursor.execute("INSERT INTO categories(name) VALUES( :name)" , data )
			self.connection.commit()
		else:
			print('This category already exists')


	def list(self):
		print('----------')
		print('Categories')
		print('----------')
		self.cursor.execute( "SELECT * FROM categories" )
		for row in self.cursor:
			print( row )
		print('----------')
		