#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from Tkinter import *   ## notice capitalized T in Tkinter 
except ImportError:
    from tkinter import *   ## notice here too

try:
    import tkMessageBox
except ImportError:
    import tkMessageBox


import ttk # for tree view
import re # for regex

from classes.task import Task
from classes.category import Category



class Interface(Frame):
	WIDTH = 300
	HEIGHT = 300


	def __init__(self):
		self.fenetre = Tk()
		self.fenetre.title("Pomodores manager")
		self.fenetre.geometry("{}x{}".format(self.WIDTH , self.HEIGHT))

		Frame.__init__(self)
		self.pack()
		self._init_menu()

		self.view_categories()




	def title(self, string):
		self.label( string , ("Helvetica", 16) )


	def input(self ):
		new_input = Entry(self)
		new_input.pack()
		return new_input

	def button(self, string , command):
		new_button = Button(self, text =string, command=command)
		new_button.pack()

	def label(self , string , font=("Helvetica", 12) ):
		new_label = Label( self , text=string , font=font)
		new_label.pack()


	def show(self):
		self.fenetre.mainloop()

		

	def _init_menu(self):


		"""
		a menu to make somthing like that:

		+--File
		|	+--Add
		|	|	+--Task
		|	|	+--Category
		|	+--Quit
		|
		+--Edit
		|	+--Settings
		|
		+--?
			+--about

		"""


		menubar = Menu(self.fenetre)



		menu_file = Menu(menubar, tearoff=0)
		submenu_add = Menu(menu_file, tearoff=0)
		submenu_add.add_command(label="task", command=self.add_task )
		submenu_add.add_command(label="category", command=self.add_category )
		menu_file.add_cascade(label='add', menu=submenu_add, underline=0)
		menu_file.add_separator()
		menu_file.add_command(label="Quit", command=self.fenetre.quit)

		menubar.add_cascade(label="File", menu=menu_file)

		menu_edit = Menu(menubar, tearoff=0)
		menu_edit.add_command(label="settings", command=self.clean )
		menubar.add_cascade(label="Edit", menu=menu_edit)


		menu_help = Menu(menubar, tearoff=0)
		menu_help.add_command(label="A propos")
		menubar.add_cascade(label="?", menu=menu_help)

		self.fenetre.config(menu=menubar)

	def clean(self):
		for widget in self.winfo_children():
			widget.destroy()


	def add_category(self):
		self.clean()
		self.title("Create a new category")
		self.label("Please enter the name of your new category")
		input = self.input()

		def callback():
			result = Category().add(input.get())
			if result != False:
				tkMessageBox.showinfo("Sucess", "Your category has benn added")
				self.view_categories()
			else:
				tkMessageBox.showerror("Error", "This category already exists!")

		self.button( "create this category" , callback )

		


	def add_task(self):
		self.clean()
		self.title("Create a new task")
		self.label("Please enter the name of your new category...")
		self.input()
		self.label("...and select a category")
		self._load_categories()


		def callback():
			print('okay #2')

		self.button( "add this task" , callback )


	def view_categories(self):
		self.clean()
		self._load_categories()


	def _load_categories(self):
		tree_categories = ttk.Treeview(self)
		tree_categories["columns"]=(0, 1)

		tree_categories.column(0, width=100)
		tree_categories.column(1, width=100)

		tree_categories.heading(0, text="name")

		
		def double_click(event):
			print('double click on {}'.format(tree_categories.selection() ))
			category_id = int(re.findall('\d+', tree_categories.selection()[0])[0])
			category = Category().find_by_id(category_id)
			print(category.name)


		i=0
		for id in Category().all_ids():
			category = Category().find_by_id(id)
			
			id_inserted = tree_categories.insert('', 'end', text=category.id, values=(category.name))

			for task_id in category.tasks_id():
				task = Task().find_by_id(task_id[0])
				tree_categories.insert( id_inserted , category.id , text=task.name, values=(category.id) )

			tree_categories.insert( id_inserted , category.id , text='add a Task' )
			
			i+=1
		tree_categories.bind('<Double-Button-1>' , double_click )
		tree_categories.pack()
