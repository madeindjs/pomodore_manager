from classes.database import Database

class Pomodore(Database):

	def __init__(self):
		Database.__init__(self)
		self.cursor.execute(
			"CREATE TABLE IF NOT EXISTS pomodores( " + 
				"id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, "+
				"task_id INTERGER NOT NULL, "+
				"category_id INTERGER NOT NULL, "+
				"date DATETIME ) ")


	def find(self):
		print("hello world")


	# def add(self ,  name ):
	# 	data = { "name" : name }
	# 	self.cursor.execute("INSERT INTO categories( name) VALUES( :name)" , data )
	# 	self.connection.commit()

	def list(self):
		self.cursor.execute( "SELECT * FROM pomodores" )
		for row in self.cursor:
			print( row )