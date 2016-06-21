#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

class Setting():

	FONT_TITLE=("Helvetica", 16)
	FONT_TEXT=("Helvetica", 12)
	FONT_DONE=("Helvetica", 10 , 'overstrike')
	FONT_UNDONE=FONT_TEXT
	PADDING=5
	
	def __init__(self):

		with open('settings.json') as settings_file:    
			data = json.load(settings_file)
			self = data
