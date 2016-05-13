#!/usr/bin/env python
# -*- coding: utf-8 -*-

#import tkinter interface
try:
    from Tkinter import *
    import ttk
except ImportError:
    from tkinter import *
    from tkinter import ttk



class Pomodore(Frame):

	WIDTH=500

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

	TIMER=20
	INTERVAL=1


	def __init__(self, task):

		#init the main view
		self.fenetre = Tk()
		self.fenetre.configure(background=self.COLOR_BKG)
		self.fenetre.title("Pomodore for {}".format(task.name))

		Frame.__init__(self , background=self.COLOR_BKG)
		self.pack(fill=BOTH)

		#checkbox for task.status
		Label(self.fenetre, text="done",
			font=self.FONT_TEXT , 
			foreground=self.COLOR_TXT, 
			background=self.COLOR_BKG ).pack()

		self.progress = ttk.Progressbar(self.fenetre, orient="horizontal", length=500, mode="determinate")
		self.progress["maximum"] = self.TIMER
		self.progress.pack()

		self.button = Button(self.fenetre , text="start", command=self.start)
		self.button.pack()

		self.time_spend = 0

		self.fenetre.mainloop()


	def start(self):

		if self.time_spend < self.TIMER:
			self.time_spend += self.INTERVAL
			self.progress["value"] = self.time_spend
			self.after(100, self.start)
		else:

			database = Database()
			data = { "name" : self.name , "node_id" : self.node_id }
			self.database.cursor.execute("INSERT INTO pomodores(node_id, name) VALUES(:node_id, :name)" , data )


			print("pomodore finished")
			self.fenetre.destroy()
			self.destroy()
