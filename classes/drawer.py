#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Drawer:
	MAX_SIZE = 70
	SEPARATOR_CHAR = '_'

	def header(self , string = SEPARATOR_CHAR):
		print('\n\n\n')
		self.subheader(string)
		self.line()

	def subheader(self , string = SEPARATOR_CHAR , separator = SEPARATOR_CHAR ):
		print('\n')
		nb_separator = int ( ( self.MAX_SIZE - len(string) ) /2 )
		print("{0}{1}{0}".format( separator*nb_separator ,  string ))

	def line(self):
		print(self.SEPARATOR_CHAR*self.MAX_SIZE)

	def list(self, list):
		for key in list:
			print( "    #{} - {}".format( key , list[key] ) )

	def success_msg(self):
		self.subheader( "COMPLETED" , ' ')
