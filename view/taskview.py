#!/usr/bin/env python
# -*- coding: utf-8 -*-

#import tkinter interface
try:
    from Tkinter import *
    import ttk
    print('import Tkinter')
except ImportError:
    from tkinter import *
    from tkinter import ttk
    print('import tkinter')

import re # for regex
from classes.task import Task
from view.setting import Setting
from view.pomodoreview import PomodoreView



class TaskView(Frame):



	def __init__(self):

		#init the main view
		Frame.__init__(self , background=Setting.COLOR_BKG)
		self.pack(fill=BOTH)
		self._init_context_menu()

		

		#init the tree
		ttk.Style().configure( "Treeview", 
			background=Setting.COLOR_BKG, 
			foreground=Setting.COLOR_TXT, 
			fieldbackground=Setting.COLOR_BKG)
		self.tree_holder = Frame(self)
		self.tree_holder.pack(fill=BOTH)
		self._tree()


	def _tree(self):

		#I begin to destroy the old treeview if he exist
		for widget in self.tree_holder.winfo_children():
			widget.destroy()
		
		self.tree = ttk.Treeview(self.tree_holder)

		self.tree["columns"]=("id","pomodores")
		self.tree["displaycolumns"]=("pomodores")
		self.tree.column("pomodores", width=100 )

		self.tree.heading("pomodores", text="pomodores")

		# and each tasks in cascade
		for task in Task.all():
			self.tree.insert( '', 'end', "task_{}".format(task.id), 
				value=(task.id, task.count_pomodores()), text=task.name, tag='status_{}'.format(task.status), open=not bool(task.status))

			if task.node_id != 0:
				self.tree.move("task_{}".format(task.id), "task_{}".format(task.node_id), 'end')

		#I begin to apply different style for different status
		self.tree.tag_configure('status_0', font=Setting.FONT_UNDONE , foreground=Setting.COLOR_UNDONE )
		self.tree.tag_configure('status_1', font=Setting.FONT_DONE , foreground=Setting.COLOR_DONE)

		self.tree.bind('<ButtonRelease-3>' , self.show_context_menu )
		self.tree.bind('<ButtonRelease-1>' , self.show_details )

		self.tree.pack(fill=X , side=TOP)

	def _init_context_menu(self):
		self.context_menu = Menu(self, tearoff=0)
		self.context_menu.add_command( label ='add', command=self.add)
		self.context_menu.add_separator()
		self.context_menu.add_command( label ='delete', command=self.delete)
		self.pack()

	def show_details(self, e):
		#refresh the view
		try:
			self.details.destroy()
		except AttributeError:
			pass
			
		task = self._get_select_item()
		if task:

			#add variables values for checkbox & entry
			status_value = IntVar()
			name_value = StringVar()
			status_value.set(task.status)
			name_value.set(task.name)

			#call back when something changed
			#when somthing change, we update the treeView & the object
			def callback(a=None,b=None,c=None):
				task.name = name_value.get()
				task.description = self.details.description.get("1.0",END)
				task.status = status_value.get()
				task.update()
				self._tree()


			self.details = LabelFrame(self, text='Details', 
				relief=FLAT,
				padx=Setting.PADDING, pady=Setting.PADDING, 
				font=Setting.FONT_TITLE ,
				foreground=Setting.COLOR_TXT, background=Setting.COLOR_BKG)

			self.details.actions = Frame(self.details , background=Setting.COLOR_BKG)


			#checkbox for task.status
			self.details.status = Checkbutton(self.details.actions, text="done", variable=status_value, 
				font=Setting.FONT_TEXT , 
				fg=Setting.COLOR_TXT, 
				background=Setting.COLOR_BKG, selectcolor=Setting.COLOR_INP , command=callback).pack()

			Button(self.details.actions, text="start", command=self.start).pack(fill=X)
			Button(self.details.actions, text="subtask", command=self.add).pack(fill=X)
			Button(self.details.actions, text="delete", command=self.delete).pack(fill=X)

			self.details.actions.pack(fill=X, side=RIGHT)


			#Entry for task.name
			self.details.name = Entry(self.details, textvariable=name_value,
				font=Setting.FONT_TITLE , 
				foreground=Setting.COLOR_TXT, 
				background=Setting.COLOR_INP )
			self.details.name.pack(fill=X)

			#Text for task.description
			self.details.description = Text(self.details, 
				font=Setting.FONT_TEXT , 
				foreground=Setting.COLOR_TXT, 
				background=Setting.COLOR_INP,  # height=5
				)
			self.details.description.insert("1.0", task.description)
			self.details.description.pack(fill=X)

			name_value.trace("w", callback )
			self.details.description.bind('<Key>' , callback )
			self.details.pack(fill=X )

		else:
			print('task not found')



	def show_context_menu(self ,e):
		self.context_menu.post(e.x_root, e.y_root)


	def add(self):
		# I retrive what object selected is
		item_properties = self.tree.item( self.tree.focus() )

		node_id = 0
		try:
			node_id = int(item_properties['values'][0])
		except:
			node_id = 0

		new_task = Task()
		new_task.name = 'no name'
		new_task.description = 'no description'
		new_task.node_id = node_id
		new_task.status = 0
		new_task.add()
		self._tree()



	def delete(self):
		task = self._get_select_item()
		task.delete()
		self._tree()

	def _get_select_item(self):
		try:
			item_properties = self.tree.item( self.tree.focus() )
			id = int(item_properties['values'][0])
			task = Task(id)
			if task:
				print("nb pomodores = {}".format(task.count_pomodores()))
				return task
			else:
				return False

		except IndexError:
			print('No item selected')
			return False


	def start(self):
		self.taskview = PomodoreView(self._get_select_item())
