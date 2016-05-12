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

	STYLE_TITLE = ("Helvetica", 16)
	STYLE_TEXT = ("Helvetica", 12)
	STYLE_TASK_DONE = ("Helvetica", 10 , 'overstrike')

	STYLE_PAD = 5
	BKG_COLOR= '#34495E'
	TXT_COLOR= '#ECF0F1'
	INP_COLOR='#22313F'


	def __init__(self):

		self.fenetre = Tk()
		self.fenetre.configure(background=self.BKG_COLOR)
		self.fenetre.title("Pomodores manager")

		self.fenetre.geometry("{}x{}".format(self.WIDTH , self.HEIGHT))

		Frame.__init__(self)
		self.pack(fill=BOTH)

		self._init_menu()
		self._init_context_menu()
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
		menu_edit.add_command(label="settings", command=self.clean )
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
		# try:
		# 	self.tree.destroy()
		# except:
		# 	pass

		for widget in self.tree_holder.winfo_children():
			widget.destroy()
		

		ttk.Style().configure(
			"Treeview", 
			background=self.BKG_COLOR, 
			foreground=self.TXT_COLOR, 
			fieldbackground=self.BKG_COLOR)
		
		self.tree = ttk.Treeview(self.tree_holder)

		for task in Task.all():
			self.tree.insert( '', 'end' , "task_{}".format(task.id) , value=task.id , text=task.name, tag='status_{}'.format(task.status), open=True)

			if task.node_id != 0:
				self.tree.move("task_{}".format(task.id), "task_{}".format(task.node_id), 'end')

		self.tree.tag_configure('status_0', font=self.STYLE_TEXT)
		self.tree.tag_configure('status_1', font=self.STYLE_TASK_DONE )

		self.tree.bind('<ButtonRelease-3>' , self.show_context_menu )
		self.tree.bind('<ButtonRelease-1>' , self.show_details )
		self.tree.pack(fill=X , side=TOP)

	def show_details(self, e):
		#refresh the view
		try:
			self.details.destroy()
		except AttributeError:
			pass
			

		#found & initialize item
		try:
			item_properties = self.tree.item( self.tree.focus() )
			id = int(item_properties['values'][0])
			task = Task(id)

			self.details = LabelFrame(self, text=task.describe(), 
				relief=FLAT,
				padx=self.STYLE_PAD, pady=self.STYLE_PAD, 
				font=self.STYLE_TITLE ,
				foreground=self.TXT_COLOR, background=self.BKG_COLOR
			)
			if task:
				status_value = IntVar()
				status_value.set(task.status)


				def callback(e=None):
					task.description = self.details.description.get("1.0",END)
					task.status = status_value.get()
					print('task status changed, now its {}'.format(status_value.get()))
					task.update()
					self._tree()


				# status_value.set(task.status)

				self.details.status = Checkbutton(self.details, text="done", variable=status_value, 
					font=self.STYLE_TEXT , 
					fg=self.TXT_COLOR, 
					background=self.BKG_COLOR, selectcolor='red' , command=callback).pack(side=LEFT)

				self.details.description = Text(self.details, 
					font=self.STYLE_TEXT , 
					foreground=self.TXT_COLOR, 
					background=self.INP_COLOR, 
					# height=5
					)
				self.details.description.insert("1.0", task.description)
				self.details.description.pack(fill=X)


				self.details.description.bind('<Key>' , callback )



		except IndexError:
			print('No item selected')

		
		self.details.pack(fill=X )



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