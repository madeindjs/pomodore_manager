#!/usr/bin/env python
# -*- coding: utf-8 -*-

#import tkinter interface
try:
    from Tkinter import *
    import ttk
except ImportError:
    from tkinter import *
    from tkinter import ttk

import time
import datetime

from classes.pomodore import Pomodore
from view.setting import Setting


class PomodoreView(Frame):

	TIMER=20
	INTERVAL=1


	def __init__(self, task):

		#init the main view
		self.fenetre = Tk()
		self.fenetre.configure(background=Setting.COLOR_BKG)
		self.fenetre.title("Pomodore for {}".format(task.name))

		Frame.__init__(self , background=Setting.COLOR_BKG)
		self.pack(fill=BOTH)

		#checkbox for task.status
		Label(self.fenetre, text="done",
			font=Setting.FONT_TEXT , 
			foreground=Setting.COLOR_TXT, 
			background=Setting.COLOR_BKG ).pack()

		self.progress = ttk.Progressbar(self.fenetre, orient="horizontal", length=500, mode="determinate")
		self.progress["maximum"] = self.TIMER
		self.progress.pack()

		self.button = Button(self.fenetre , text="start", command=self.start)
		self.button.pack()

		self.task = task
		self.time_spend = 0

		self.fenetre.mainloop()

	def _build_form():
		def show_details(self, e):
		#refresh the view
		try:
			self.details.destroy()
		except AttributeError:
			pass
			
		task = self._get_select_item()
		Writter.event('clicked on => {}'.format(self.tree.focus()))
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


	def start(self):

		if self.time_spend < self.TIMER:
			self.time_spend += self.INTERVAL
			self.progress["value"] = self.time_spend
			self.after(100, self.start)

		else:
			self.pomodore.add()
			self.fenetre.destroy()
			self.destroy()