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
	"""a pomodore view"""



	def __init__(self, pomodore):

		self.pomodore = pomodore

		#init the main view
		self.fenetre = Tk()
		self.fenetre.configure(background=Setting.COLOR_BKG)
		self.fenetre.title("Pomodore for {}".format(self.pomodore.task.name))

		Frame.__init__(self , background=Setting.COLOR_BKG)
		self.pack(fill=BOTH)

		#checkbox for task.status
		Label(self.fenetre, text="done",
			font=Setting.FONT_TEXT , 
			foreground=Setting.COLOR_TXT, 
			background=Setting.COLOR_BKG ).pack()

		self.progress = ttk.Progressbar(self.fenetre, orient="horizontal", length=500, mode="determinate")
		self.progress["maximum"] = Pomodore.timer
		self.progress.pack()

		self.button = Button(self.fenetre , text="start", command=self.start)
		self.button.pack()

		self.time_spend = 0

		self.fenetre.mainloop()


	def start(self):
		"""start the pomodore"""

		if self.time_spend < Pomodore.timer :
			self.time_spend += Pomodore.interval
			self.progress["value"] = self.time_spend
			self.after(100, self.start)

		else:
			self.pomodore.add()
			self.fenetre.destroy()
			self.destroy()