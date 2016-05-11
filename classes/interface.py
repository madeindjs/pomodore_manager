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


		self.context_menu.add_command( label ='add', command=self.add)
		self.context_menu.add_separator()
		self.context_menu.add_command( label ='delete', command=self.delete)
		self.context_menu.add_command( label ='rename', command=self.rename)
		self.pack()

	def _build_tree(self):
		self.clean()

		
		self.tree = ttk.Treeview(self)
		self.tree["columns"]=(0, 1)

		self.tree.heading(0, text="name")

		self.buttons = Frame(self)

		for task in Task.all():
			self.tree.insert( '', 'end' , "task_{}".format(task.id) , value=task.id , text=task.name)

			if task.node_id != 0:
				self.tree.move("task_{}".format(task.id), "task_{}".format(task.node_id), 'end')

		self.tree.bind('<Button-3>' , self.show_context_menu )
		self.tree.bind('<Button-1>' , self.get_item_properties )
		self.tree.pack(fill=BOTH)

		
	def get_item_properties(self , e):
		item_properties = self.tree.item( self.tree.focus() )
		print(item_properties)

	def clean(self):
		for widget in self.winfo_children():
			widget.destroy()


	def show_context_menu(self ,e):
		self.context_menu.post(e.x_root, e.y_root)


	def start_task(self):
		messagebox.showinfo('Soon ;)')


	def add(self):
		# I retrive what object selected is
		item_properties = self.tree.item( self.tree.focus() )

		node_id = 0
		try:
			node_id = int(item_properties['values'][0])
		except:
			node_id = 0

		Task(node_id=node_id)
		self._build_tree()


	def rename(self):
		# I get value
		new_name = askstring('Set a new name', "prompt")
		item_properties = self.tree.item( self.tree.focus() )

		try:
			id = int(item_properties['values'][0])
			Task(id).rename(new_name)
		except:
			messagebox.showerror('Error','An error occur..')

		self._build_tree()



	def delete(self):
		messagebox.showinfo('Soon ;)')