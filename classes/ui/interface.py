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


try:
	import tkMessageBox
except:
	print('tkMessageBox not initialize..')

try:
	from tkinter import messagebox
	from tkinter.simpledialog import askstring
except:
	print('messagebox not initialize..')


from classes.objects.task import Task
from classes.ui.taskview import Taskview
from classes.ui.setting import Setting



class Interface(Frame):



	def __init__(self):

		#init the main view
		self.window = Tk()
		self.window.configure(background=Setting.COLOR_BKG)
		self.window.title("Pomodores manager")
		self.window.geometry("{}x{}".format(Setting.WIDTH , Setting.HEIGHT))

		Frame.__init__(self , background=Setting.COLOR_BKG)
		self.pack(fill=BOTH)
		self._init_menu()

		self.task_view = Taskview().pack()

		self.window.mainloop()


	def _init_menu(self):

		menubar = Menu(self.window)

		menu_file = Menu(menubar, tearoff=0)
		menu_file.add_separator()
		menu_file.add_command(label="Quit", command=self.window.quit)

		menubar.add_cascade(label="File", menu=menu_file)

		menu_edit = Menu(menubar, tearoff=0)
		menu_edit.add_separator()
		menu_edit.add_command(label="Setting" )
		menubar.add_cascade(label="Edit", menu=menu_edit)

		menu_help = Menu(menubar, tearoff=0)
		menu_help.add_command(label="A propos")
		menubar.add_cascade(label="?", menu=menu_help)

		self.window.config(menu=menubar)
