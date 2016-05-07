#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from Tkinter import *   ## notice capitalized T in Tkinter 
except ImportError:
    from tkinter import *   ## notice here too

from tkMessageBox import *



class Interface(Frame):
	WIDTH = 768
	HEIGHT = 576

	def __init__(self):
		self.fenetre = Tk()
		Frame.__init__(self, self.fenetre, width=self.WIDTH, height=self.HEIGHT)
		self.pack(fill=BOTH)
		self._init_menu()

	def add_label(self):
		new_label = Label( self , text='string')
		new_label.pack()
		return new_label

	def add_checkbox(self, string):
		checkbutton = Checkbutton( self, text=string )
		checkbutton.pack()
		return checkbutton

	def add_list(self, list):
		new_list = Listbox(self)
		i=1
		for item in list:
			new_list.insert(i,item)
			i+=1
		new_list.pack()
		return new_list

	def show(self):
		self.fenetre.mainloop()

	def _init_menu(self):
		menubar = Menu(self.fenetre)

		menu1 = Menu(menubar, tearoff=0)
		menu1.add_command(label="Créer", command=self.add_label )
		menu1.add_command(label="Editer", command=self.add_label )
		menu1.add_separator()
		menu1.add_command(label="Quitter", command=self.fenetre.quit)
		menubar.add_cascade(label="Fichier", menu=menu1)

		menu2 = Menu(menubar, tearoff=0)
		menu2.add_command(label="start")
		menubar.add_cascade(label="Pomodores", menu=menu2)

		menu3 = Menu(menubar, tearoff=0)
		menu3.add_command(label="add")
		menu3.add_command(label="list")
		menubar.add_cascade(label="Tasks", menu=menu3)

		menu4 = Menu(menubar, tearoff=0)
		menu4.add_command(label="add")
		menu4.add_command(label="list")
		menubar.add_cascade(label="Categories", menu=menu4)

		menu5 = Menu(menubar, tearoff=0)
		menu5.add_command(label="A propos")
		menubar.add_cascade(label="?", menu=menu5)

		self.fenetre.config(menu=menubar)

