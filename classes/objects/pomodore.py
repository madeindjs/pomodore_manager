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

from classes.objects.database import Database
from classes.ui.setting import Setting


class Pomodore(Frame):


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


	def start(self):

		if self.time_spend < self.TIMER:
			self.time_spend += self.INTERVAL
			self.progress["value"] = self.time_spend
			self.after(100, self.start)
		else:
			data = { "task_id" : self.task.id , "date" : datetime.datetime.today() }
			
			database = Database()
			database.cursor.execute("INSERT INTO pomodores(task_id, date) VALUES(:task_id, :date)" , data )
			database.connection.commit()

			self.fenetre.destroy()
			self.destroy()