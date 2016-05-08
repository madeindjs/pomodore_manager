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


import ttk

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

	def title(self, string):
		self.label( string , ("Helvetica", 16) )

	def text(self , string ):
		new_text = Text(self)
		new_text.insert(INSERT, string)
		new_text.pack()

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

	def checkbox(self, string):
		checkbutton = Checkbutton( self, text=string )
		checkbutton.pack()

	def list(self, list):
		new_list = Listbox(self)
		i=1
		for item in list:
			new_list.insert(i,item)
			i+=1
		new_list.pack()



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
		+--View
		|	+--categories
		|	+--tasks
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

		menu_view = Menu(menubar, tearoff=0)
		menu_view.add_command(label="pomodores")
		menu_view.add_command(label="tasks", command=self.view_tasks)
		menu_view.add_command(label="categories", command=self.view_categories)
		menubar.add_cascade(label="View", menu=menu_view)

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
		tree = ttk.Treeview(self)
		tree["columns"]=(1, 2)

		tree.column(1, width=100)
		tree.column(2, width=100)

		tree.heading(1, text="name")
		tree.heading(2, text="Nb tasks")

		def double_click(event):
			print('double click on {}'.format(event.widget.selection()))

		def simple_click(event):
			print('simple click on {}'.format(event.widget.selection()))



		i=0
		for id in Category().all_ids():
			category = Category().find_by_id(id)
			tree.insert( "" , i, text=category.id, values=(category.name,"This is a description"))
			
			i+=1
		tree.bind('<Double-Button-1>' , double_click )
		tree.bind('<Button-1>' , simple_click )
		tree.pack()



		

	def view_tasks(self):
		tree = ttk.Treeview(self)
		 
		tree["columns"]=("one","two")
		tree.column("one", width=100 )
		tree.column("two", width=100)
		tree.heading("one", text="coulmn A")
		tree.heading("two", text="column B")
		 
		tree.insert("" , 0,    text="Line 1", values=("1A","1b"))
		 
		id2 = tree.insert("", 1, "dir2", text="Dir 2")
		tree.insert(id2, "end", "dir 2", text="sub dir 2", values=("2A","2B"))
		 
		##alternatively:
		tree.insert("", 3, "dir3", text="Dir 3")
		tree.insert("dir3", 3, text=" sub dir 3",values=("3A"," 3B"))
		 
		tree.pack()
		self.mainloop()
		self.list(Task().list())

	def view_task(self):
		pass


