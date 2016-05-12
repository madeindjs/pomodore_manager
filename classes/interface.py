#!/usr/bin/env python
# -*- coding: utf-8 -*-

#import tkinter interface
try:
    from Tkinter import *
    from ttk import *
    print('import Tkinter')
except ImportError:
    from tkinter import *
    from tkinter import ttk
    print('import tkinter')


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

	FONT_TITLE = ("Helvetica", 16)
	FONT_TEXT = ("Helvetica", 12)

	FONT_DONE = ("Helvetica", 10 , 'overstrike')
	FONT_UNDONE = FONT_TEXT

	PADDING= 5

	COLOR_BKG='#34495E'
	COLOR_TXT='#ECF0F1'
	COLOR_INP='#22313F'



	COLOR_DONE='#1E824C'
	COLOR_UNDONE=''


	def __init__(self):

		#init the main view
		self.fenetre = Tk()
		self.fenetre.configure(background=self.COLOR_BKG)
		self.fenetre.title("Pomodores manager")
		self.fenetre.geometry("{}x{}".format(self.WIDTH , self.HEIGHT))

		Frame.__init__(self)
		self.pack(fill=BOTH)
		self._init_menu()
		self._init_context_menu()

		#init the tree
		ttk.Style().configure(
			"Treeview", 
			background=self.COLOR_BKG, 
			foreground=self.COLOR_TXT, 
			fieldbackground=self.COLOR_BKG)
		self.tree_holder = Frame(self)
		self.tree_holder.pack(fill=BOTH)
		self._tree()

		self.fenetre.mainloop()


	def _init_menu(self):

		menubar = Menu(self.fenetre)

		menu_file = Menu(menubar, tearoff=0)
		menu_file.add_separator()
		menu_file.add_command(label="Quit", command=self.fenetre.quit)

		menubar.add_cascade(label="File", menu=menu_file)

		menu_edit = Menu(menubar, tearoff=0)
		menu_edit.add_separator()
		menu_edit.add_command(label="settings" )
		menubar.add_cascade(label="Edit", menu=menu_edit)

		menu_help = Menu(menubar, tearoff=0)
		menu_help.add_command(label="A propos")
		menubar.add_cascade(label="?", menu=menu_help)

		self.fenetre.config(menu=menubar)



	def _init_context_menu(self):
		self.context_menu = Menu(self.fenetre, tearoff=0)
		self.context_menu.add_command( label ='add', command=self.add)
		self.context_menu.add_separator()
		self.context_menu.add_command( label ='delete', command=self.delete)
		self.context_menu.add_command( label ='rename', command=self.rename)
		self.pack()

	def _tree(self):

		#I begin to destroy the old treeview if he exist
		for widget in self.tree_holder.winfo_children():
			widget.destroy()
		
		self.tree = ttk.Treeview(self.tree_holder)

		# and each tasks in cascade
		for task in Task.all():
			self.tree.insert( '', 'end', "task_{}".format(task.id), 
				value=task.id, text=task.name, tag='status_{}'.format(task.status), open=not bool(task.status))

			if task.node_id != 0:
				self.tree.move("task_{}".format(task.id), "task_{}".format(task.node_id), 'end')

		#I begin to apply different style for different status
		self.tree.tag_configure('status_0', font=self.FONT_UNDONE , foreground=self.COLOR_UNDONE )
		self.tree.tag_configure('status_1', font=self.FONT_DONE , foreground=self.COLOR_DONE)

		self.tree.bind('<ButtonRelease-3>' , self.show_context_menu )
		self.tree.bind('<ButtonRelease-1>' , self.show_details )

		self.tree.pack(fill=X , side=TOP)

	def show_details(self, e):
		#refresh the view
		try:
			self.details.destroy()
		except AttributeError:
			pass
			

		try:
			#found the item
			item_properties = self.tree.item( self.tree.focus() )
			id = int(item_properties['values'][0])
			task = Task(id)


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
					padx=self.PADDING, pady=self.PADDING, 
					font=self.FONT_TITLE ,
					foreground=self.COLOR_TXT, background=self.COLOR_BKG)

				#checkbox for task.status
				self.details.status = Checkbutton(self.details, text="done", variable=status_value, 
					font=self.FONT_TEXT , 
					fg=self.COLOR_TXT, 
					background=self.COLOR_BKG, selectcolor=self.COLOR_INP , command=callback).pack(side=LEFT)

				#Entry for task.name
				self.details.name = Entry(self.details, textvariable=name_value,
					font=self.FONT_TITLE , 
					foreground=self.COLOR_TXT, 
					background=self.COLOR_INP )
				self.details.name.pack(fill=X)

				#Text for task.description
				self.details.description = Text(self.details, 
					font=self.FONT_TEXT , 
					foreground=self.COLOR_TXT, 
					background=self.COLOR_INP,  # height=5
					)
				self.details.description.insert("1.0", task.description)
				self.details.description.pack(fill=X)

				name_value.trace("w", callback )
				self.details.description.bind('<Key>' , callback )
				self.details.pack(fill=X )
			else:
				print('task not found')
		except IndexError:
			print('No item selected')


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
		self._tree()


	def rename(self):
		# I get value
		item_properties = self.tree.item( self.tree.focus() )

		try:
			id = int(item_properties['values'][0])
			task = Task(id)
			task.name = askstring('Rename', 'set a new name:' , initialvalue=task.name)
			task.update()
		except:
			messagebox.showerror('Error','An error occur..')

		self._tree()



	def delete(self):
		item_properties = self.tree.item( self.tree.focus() )

		id = int(item_properties['values'][0])
		Task(id).delete()

		self._tree()