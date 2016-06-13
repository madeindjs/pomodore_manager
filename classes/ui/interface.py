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
	from Tix import *
except ImportError:
  	from tkinter.tix import *
# try:
# 	from ttk import *
# except ImportError:
#   	from tkinter.ttk import *
try:
	from tkMessageBox import *
except ImportError:
  	from tkinter.messagebox import *
# try:
# 	from tkColorChooser import *
# except ImportError:
#   	from tkinter.colorchooser import *
# try:
# 	from tkFileDialog import *
# except ImportError:
#   	from tkinter.filedialog import *
# try:
# 	from tkCommonDialog import *
# except ImportError:
#   	from tkinter.commondialog import *
try:
	from tkSimpleDialog import *
except ImportError:
  	from tkinter.simpledialog import *
# try:
# 	from tkFont import *
# except ImportError:
#   	from tkinter.font import *
# try:
# 	from Tkdnd import *
# except ImportError:
#   	from tkinter.dnd import *
# try:
# 	from ScrolledText import *
# except ImportError:
#   	from tkinter.scrolledtext import *



from classes.ui.taskview import TaskView
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

		self.task_view = TaskView().pack()

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
