#!/usr/bin/env python
# -*- coding: utf-8 -*-

#import tkinter interface
try:
    from Tkinter import *
    from Tkinter import ttk
except ImportError:
    from tkinter import *
    from tkinter import ttk


try:
    import tkMessageBox
except ImportError:
    from tkinter import messagebox


import re # for regex

from classes.task import Task
from classes.category import Category



class Interface(Frame):
	WIDTH = 300
	HEIGHT = 300

	TITLE = ("Helvetica", 16)
	TEXT = ("Helvetica", 12)



	def __init__(self):
		self.fenetre = Tk()
		self.fenetre.title("Pomodores manager")
		self.fenetre.geometry("{}x{}".format(self.WIDTH , self.HEIGHT))

		Frame.__init__(self)
		self.pack()
		self._init_menu()

		self.view_categories()




	def title(self, string):
		Label( string , self.TITLE ).pack()


	def input(self ):
		new_input = Entry(self).pack()

	def button(self, string , command):
		Button(self, text =string, command=command).pack()

	def label(self , string  ):
		Label( self , text=string , font=self.TEXT).pack()


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
		# self._load_categories()


		def callback():
			print('okay #2')

		self.button( "add this task" , callback )


	def view_categories(self):
		self.clean()

		
		tree = ttk.Treeview(self)
		tree["columns"]=(0, 1)

		tree.heading(0, text="name")

		buttons = Frame(self)

		def callback(event, frame=buttons):

			#I clean old buttons
			for old_button in frame.winfo_children():
				old_button.destroy()

			# I retrive what object selected is
			item_properties = tree.item( tree.focus() )
			item_tag = item_properties['tags'][0]

			#if it's a category, we insert start, edit, delete button
			if item_tag == 'task':
				Button( frame , text ='start', command=callback ).pack()
				Button( frame , text ='edit', command=callback ).pack()
				Button( frame , text ='delete', command=callback ).pack()

			#if it's a task, we insert add, edit, delete button
			elif item_tag == 'category':
				Button( frame , text ='add a new task', command=callback ).pack()
				Button( frame , text ='edit', command=callback ).pack()
				Button( frame , text ='delete', command=callback ).pack()

			frame.pack()
		#CALLBACK END


		# I insert all categoriesin tree
		for id in Category().all_ids():
			category = Category().find_by_id(id)
			id_inserted = tree.insert('', 'end', text=category.name , tags='category')

			#in each category I insert tasks
			for task_id in category.tasks_id():
				task = Task().find_by_id(task_id[0])
				tree.insert( id_inserted , 'end' , text=task.name, values=(category.id) , tags='task' )

		tree.bind('<Double-Button-1>' , callback )
		tree.pack()