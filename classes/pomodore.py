from classes.database import Database
from classes.task import Task

class Pomodore(Database):

	DATABASE_NAME = 'pomodores'

	def __init__(self):
		Database.__init__(self)
		self.cursor.execute(
			"CREATE TABLE IF NOT EXISTS pomodores( " + 
				"id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, "+
				"task_id INTERGER NOT NULL, "+
				"category_id INTERGER NOT NULL, "+
				"date DATETIME ) ")


	def add():
		#ask wich task
		task = Task()
		task.list()
		try:
			answer = int( input('Wich task do you work with (Enter nly the number)? ') )
			task.find_by_id(answer)
			print("You chose {}".format( task.describe()) )
		except:
			print("Please enter a valid value")
		#start the prompt
		#add to database