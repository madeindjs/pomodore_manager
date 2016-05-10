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
	from tkinter.simpledialog import askstring
	# messagebox.askquestion('title','question')
except:
	print('messagebox not initialize..')




import re # for regex

from classes.task import Task
from classes.node import Node



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
		self.pack(fill=BOTH)
		self._init_menu()
		self._init_context_menu()

		self._build_tree()
		self.fenetre.mainloop()


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

	def _init_toolbar(self):
		toolbar = Frame(self.parent, bd=1, relief=RAISED)


	def _init_context_menu(self):
		self.context_menu = Menu(self.fenetre, tearoff=0)

		self.context_menu.add_command( label ='rename', command=self.renam_item)
		self.context_menu.add_command( label ='delete', command=self.delete_task)
		self.context_menu.add_separator()

		submenu = Menu(self.context_menu)
		submenu.add_command( label ='folder', command=self.add_category)
		submenu.add_command( label ='task', command=self.add_task)
		self.context_menu.add_cascade(label='new', menu=submenu)
		self.pack()

	def _build_tree(self):
		self.clean()

		
		self.tree = ttk.Treeview(self)
		self.tree["columns"]=(0, 1)

		self.tree.heading(0, text="name")

		self.buttons = Frame(self)


		for node in Node().all():
			self.tree.insert( '', 'end' , "node_{}".format(node.id) , text='node')

			for task in node.tasks():
				self.tree.insert( '', 'end' , "task_{}".format(task.id) , text=task.name)
				self.tree.move("task_{}".format(task.id), "node_{}".format(node.id), 'end')



		self.tree.bind('<Button-3>' , self.show_context_menu )
		self.tree.pack(fill=BOTH)

		


	def clean(self):
		for widget in self.winfo_children():
			widget.destroy()



	def show_context_menu(self ,e):
		self.context_menu.post(e.x_root, e.y_root)



	def add_category(self):
		category = Category().add('new category')
		if category:
			self._build_tree()
		else:
			messagebox.showerror('Error')

	def edit_category(self):
		messagebox.showinfo('Soon ;)')

	def delete_category(self):
		messagebox.showinfo('Soon ;)')


	def start_task(self):
		messagebox.showinfo('Soon ;)')


	def add_task(self):
		# I retrive what object selected is
		item_properties = self.tree.item( self.tree.focus() )
		item_type = item_properties['tags'][0]

		#if it's a category, we can insert a task
		if item_type == 'category':
			item_id = item_properties['tags'][1]
			category = Category(item_id)
			new_task = Task().add('new task', category)
			if new_task:
				print(new_task)
			else:
				print('Error {}'.format(new_task) )
			self._build_tree()

		else:
			messagebox.showerror('Error' , "Can't insert a task beacause it's not a category!")

	def renam_item(self):
		new_name = askstring('hello', "prompt")

		item_properties = self.tree.item( self.tree.focus() )
		item_type = item_properties['tags'][0]
		item_id = item_properties['tags'][1]

		if item_type == 'category' and item_id != None :
			category = Category(item_id)
			category.rename(new_name)
		elif item_type == 'task' and item_id != None :
			task = Task(item_id)
			task.rename(new_name)
		else:
			messagebox.showerror('Error' , "Nothing selected")

		self._build_tree()



	def delete_task(self):
		messagebox.showinfo('Soon ;)')
		



	def get_item_tag(self):
		# I retrive what object selected is
		item_properties = self.tree.item( self.tree.focus() )
		return item_properties['tags'][0]




