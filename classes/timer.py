#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import sys
from classes.drawer import Drawer

class Timer:
	MAX_SIZE = 70
	INTERVAL = .1
	PROGRESS_CHAR = '-'

	def __init__(self , time_in_ms):
		try:
			self.time = int(time_in_ms)
		except:
			self.time = 0
			print("Enter a valid integer")
		

	def start(self):
		i= 0
		
		while i < self.time*10:
			time.sleep( self.INTERVAL )
			size = int( i * self.MAX_SIZE / (self.time*10) )

			rest_time = self.time - int(i/10)
			string_rest_time = time.strftime('%M\'%S"', time.gmtime(rest_time))
			sys.stdout.write('\r[{0}] {1}'.format( self.PROGRESS_CHAR*size, string_rest_time ))
			i += 1

		Drawer().success_msg()
		return True
