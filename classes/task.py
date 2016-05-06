from classes.database import Database
from classes.category import Category
from classes.drawer import Drawer



class Task(Database):

	DATABASE_NAME = 'tasks'

	def __init__(self):
		Database.__init__(self)
		self.cursor.execute(
			"CREATE TABLE IF NOT EXISTS tasks( " + 
				"id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, "+
				"category_id INTERGER NOT NULL, "+
				"name TEXT NOT NULL  ) ")


	def add(self ,  name , category):
		# check before if this category already exist
		if self.find_by_name(name) == False:
			data = { "name" : name , "category_id" : category.id }
			self.cursor.execute("INSERT INTO tasks(category_id, name) VALUES(:category_id, :name)" , data )
			self.connection.commit()
			#set up & check if saved succesfully
			if self.find_by_name(name):
				Drawer().success_msg()
				return self
			else:
				return False

		else:
			return False


	def set(self, data):
		self.id = data[0]
		self.category = Category().find_by_id(data[1])
		self.name = data[2]
		return self

	def describe(self):
		return "Task #{} named *{}* on category *{}*".format(self.id, self.name , self.category.name)


	def count_pomodores(self):

		if not self.id is None:
			data = { 'task_id' : self.id }
			self.cursor.execute("SELECT COUNT(*) from pomodores WHERE task_id = :task_id " , data )
			result = self.cursor.fetchone()
			return result[0]
		else:
			return False

	def list(self):
		Drawer().subheader(self.DATABASE_NAME)
		self.cursor.execute( "SELECT * FROM {}".format( self.DATABASE_NAME ) )
		for row in self.cursor:
			task_temp = Task().set(row)
			print("Task N°{} # {}   | {}".format( task_temp.id , task_temp.category.name , 'o'*task_temp.count_pomodores() ))
			print("    {}\n".format(task_temp.name))
		Drawer().line()
