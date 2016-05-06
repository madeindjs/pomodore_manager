from classes.database import Database

class Category(Database):

	DATABASE_NAME = 'categories'

	def __init__(self):
		Database.__init__(self)
		self.cursor.execute(
			"CREATE TABLE IF NOT EXISTS categories( " + 
				"id INTEGER PRIMARY KEY , "+
				"name TEXT NOT NULL UNIQUE) ")


	def add(self ,  name ):
		# check before if this category already exist
		if self.find_by_name(name) == False:
			data = { "name" : name }
			self.cursor.execute("INSERT INTO categories(name) VALUES( :name)" , data )
			self.connection.commit()
		else:
			print('This category already exists')