#!/usr/bin/env python
# -*- coding: utf-8 -*-

#import tkinter interface
try:
    from Tkinter import *
    import ttk
except ImportError:
    from tkinter import *
    from tkinter import ttk


try:
	import tkMessageBox
except:
	print('tkMessageBox not initialize..')

try:
	from tkinter import messagebox
	# messagebox.askquestion('title','question')
except:
	print('messagebox not initialize..')




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
		self._init_context_menu()

		self._view()


	def _init_menu(self):

		menubar = Menu(self.fenetre)

		menu_file = Menu(menubar, tearoff=0)
		menu_file.add_separator()
		menu_file.add_command(label="Quit", command=self.fenetre.quit)

		menubar.add_cascade(label="File", menu=menu_file)

		menu_edit = Menu(menubar, tearoff=0)
		menu_edit.add_command(label="add a category", command=self.add_category )
		menu_edit.add_separator()
		menu_edit.add_command(label="settings", command=self.clean )
		menubar.add_cascade(label="Edit", menu=menu_edit)

		menu_help = Menu(menubar, tearoff=0)
		menu_help.add_command(label="A propos")
		menubar.add_cascade(label="?", menu=menu_help)

		self.fenetre.config(menu=menubar)


	def _init_context_menu(self):
		self.context_menu = Menu(self.fenetre, tearoff=0)


	def show(self):
		self.fenetre.mainloop()


	def clean(self):
		for widget in self.winfo_children():
			widget.destroy()


	def add_category(self):
		category = Category().add('new category')
		if category:
			self._view()
		else:
			messagebox.showerror('Error')

	def edit_category(self):
		messagebox.showInfos('Soon ;)')

		

	def show_context_menu(self ,e):

		self.context_menu.post(e.x_root, e.y_root)

		self.context_menu.delete(0,2)

		# I retrive what object selected is
		item_properties = self.tree.item( self.tree.focus() )
		item_tag = item_properties['tags'][0]

		#if it's a category, we insert start, edit, delete button
		if item_tag == 'task':
			self.context_menu.add_command( label ='start', command=self.fenetre.quit)
			self.context_menu.add_command( label ='edit', command=self.fenetre.quit)
			self.context_menu.add_command( label ='delete', command=self.fenetre.quit)
			self.pack()

		#if it's a task, we insert add, edit, delete button
		elif item_tag == 'category':
			self.context_menu.add_command( label ='add a new task', command=self.fenetre.quit)
			self.context_menu.add_command( label ='edit', command=self.edit_category)
			self.context_menu.add_command( label ='delete', command=self.fenetre.quit)
			self.pack()



	def _view(self):
		self.clean()

		
		self.tree = ttk.Treeview(self)
		self.tree["columns"]=(0, 1)

		self.tree.heading(0, text="name")

		self.buttons = Frame(self)


		# I insert all categoriesin tree
		for id in Category().all_ids():
			category = Category().find_by_id(id)
			id_inserted = self.tree.insert('', 'end', text=category.name , tags='category')

			#in each category I insert tasks
			for task_id in category.tasks_id():
				task = Task().find_by_id(task_id[0])
				self.tree.insert( id_inserted , 'end' , text=task.name, values=(category.id) , tags='task' )

		self.tree.bind('<Button-3>' , self.show_context_menu )
		self.tree.pack()