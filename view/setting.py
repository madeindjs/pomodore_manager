#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Setting():
	WIDTH = 300
	HEIGHT = 400

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


	def label_settings(self):
		return 'test'